"""Activa n8n sin imprimir claves, destinatarios ni respuesta privada."""
import json, os, urllib.request, urllib.error

def main():
    key=os.environ.get('N8N_SIMULATION_KEY','')
    if not key: raise SystemExit('Falta configurar el Secret N8N_SIMULATION_KEY en GitHub y la misma clave en Header Auth de n8n.')
    a=int(os.environ['PRODUCTO_A']); b=int(os.environ['PRODUCTO_B'])
    if not (1<=a<=100 and 1<=b<=80): raise SystemExit('Cantidades fuera del catálogo ficticio.')
    run_id=os.environ['GITHUB_RUN_ID']
    if not run_id.isdigit(): raise SystemExit('Identificador de ejecución inválido.')
    body={'repository':os.environ['GITHUB_REPOSITORY'],'run_id':run_id,'modo':'SIMULADO','producto_a':a,'producto_b':b}
    request=urllib.request.Request('https://mariana30.app.n8n.cloud/webhook/logismart-github-simulacion',data=json.dumps(body).encode(),headers={'Content-Type':'application/json','LogiSmart-key':key},method='POST')
    try:
        with urllib.request.urlopen(request,timeout=110) as response: result=json.load(response)
    except urllib.error.HTTPError as e:
        raise SystemExit(f'n8n respondió HTTP {e.code}. Revisar la ejecución privada de n8n; no reintentar automáticamente.') from None
    except (urllib.error.URLError,TimeoutError):
        raise SystemExit('No se pudo confirmar el resultado de n8n. Revisar su historial antes de repetir para evitar duplicados.') from None
    if isinstance(result,list) and len(result)==1: result=result[0]
    if not isinstance(result,dict) or result.get('enviado_telegram') is not True or result.get('modo')!='SIMULADO':
        raise SystemExit('n8n no confirmó el envío; revisar su historial privado.')
    if result.get('estado_final')!='PENDIENTE_APROBACION' or result.get('aprobacion_humana')!='PENDIENTE':
        raise SystemExit('Se envió el resultado, pero el caso no quedó pendiente de aprobación; revisar agentes en n8n.')
    print('Cotización ficticia procesada y envío Telegram confirmado por n8n. Aprobación humana pendiente.')

if __name__=='__main__': main()
