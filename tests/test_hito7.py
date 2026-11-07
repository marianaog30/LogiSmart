import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import hito7


class Hito7(unittest.TestCase):
    def test_mejora_y_reutilizacion(self):
        e = hito7.evidencia()
        q = e['calidad_v1_v2_mismo_caso']
        self.assertEqual(q['estado'], 'VALIDADA')
        self.assertEqual([x['validacion'] for x in q['traza'][1:]], ['FALLIDA', 'CORRECTA'])
        self.assertEqual(len({x['caso_id'] for x in q['traza'][1:]}), 1)
        self.assertEqual(q['propuesta']['total_centavos'], 351000)
        self.assertEqual(e['segundo_caso']['calidad']['propuesta']['total_centavos'], 49500)
        self.assertEqual(e['seguridad_sanitizacion']['estado'], 'LIBERADA')
        self.assertNotIn('VALOR_NO_PUBLICABLE', json.dumps(e))

    def test_rechazos(self):
        for nombre, estado in [('sin_permiso', 'DETENIDO_PERMISOS'),
                               ('costo_desconocido', 'DETENIDO_COSTO_NO_VERIFICABLE'),
                               ('presupuesto_excedido', 'DETENIDO_PRESUPUESTO'),
                               ('operacion_prohibida', 'DETENIDO_OPERACION')]:
            self.assertEqual(hito7.evidencia()[nombre]['estado'], estado)
        for a, b in [(101, 1), (True, 1), (0, 2), (2, 81)]:
            with self.assertRaises(ValueError):
                hito7.precontrol(a, b, 'H7-RECHAZO')

    def test_humano_no_se_suplanta(self):
        p = hito7.precontrol(1, 1, 'H7-HUMANO')['calidad']['propuesta']
        p['aprobacion_humana'] = 'APROBADA'
        self.assertEqual(hito7.seguridad(p, True)['estado'], 'DETENIDO_DECISION_HUMANA')

    def test_reglas_cargadas_cambian_comportamiento_y_limite(self):
        # Demuestra aplicación del archivo, no solo lectura decorativa.
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name in ['logismart-cotizar', 'logismart-revisar']:
                dest = root / 'skills' / name / 'SKILL.md'
                dest.parent.mkdir(parents=True)
                dest.write_text((hito7.ROOT / 'skills' / name / 'SKILL.md').read_text())
            file = root / 'skills/logismart-cotizar/SKILL.md'
            file.write_text(file.read_text().replace('"precio_centavos":12000', '"precio_centavos":20000').replace('"max_iteraciones":3', '"max_iteraciones":1'))
            s = {'caso_id': 'H7-REGLA', 'modo': 'SIMULADO', 'productos': [{'producto': 'Producto A', 'cantidad': 1}]}
            p = hito7.calidad(s, root=root)['propuesta']
            self.assertEqual(p['total_centavos'], 20000)
            p['total_centavos'] = 1
            self.assertEqual(hito7.calidad(s, p, root=root)['estado'], 'LIMITE_AGOTADO')


if __name__ == '__main__':
    unittest.main()
