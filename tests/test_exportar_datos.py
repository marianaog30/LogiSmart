import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('exportar', ROOT / 'scripts/exportar_datos.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class Exportacion(unittest.TestCase):
    def setUp(self):
        self.d = {'fuente':'Data Table LogiSmart', 'datos_ficticios':True,
                  'consultado_en':'2026-11-06T18:00:00Z', 'zona_horaria':'America/Mexico_City',
                  'total_registros':1, 'registros_excluidos':0,
                  'registros':[{'folio_publico':'MUESTRA-001','fecha_registro':None,
                    'productos':['Producto A'],'importe_total':None,'moneda':'MXN',
                    'estado_final':'PENDIENTE_APROBACION','aprobacion_humana':'PENDIENTE',
                    'duracion_total_ms':None,'origen':'WORKFLOW',
                    'completa_primer_intento':None,'sin_correcciones_auditoria':None}]}

    def test_lista_cerrada_y_null(self):
        self.d['credencial_de_prueba'] = 'NO_PUBLICAR'
        self.d['registros'][0]['chat_de_prueba'] = 'NO_PUBLICAR'
        r = m.sanitizar(self.d)
        self.assertNotIn('NO_PUBLICAR', str(r))
        self.assertIsNone(r['registros'][0]['importe_total'])
        self.assertIsNone(r['registros'][0]['completa_primer_intento'])

    def test_fallos_de_datos(self):
        for campo, valor in [('aprobacion_humana','APROBADA'),('importe_total',True),
                             ('importe_total',float('nan')),('completa_primer_intento',True),
                             ('fecha_registro','sin fecha'),('origen','desconocido')]:
            d = copy.deepcopy(self.d)
            d['registros'][0][campo] = valor
            with self.subTest(campo=campo,valor=valor), self.assertRaises(ValueError):
                m.sanitizar(d)
        self.d['total_registros'] = 2
        with self.assertRaises(ValueError):
            m.sanitizar(self.d)


if __name__ == '__main__':
    unittest.main()
