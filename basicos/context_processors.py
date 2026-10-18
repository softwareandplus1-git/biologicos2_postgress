# mi_app/context_processors.py

def utilidades_globales(request):

     if not request.user.is_authenticated:
        return {
            'nombreusu':'NINGUNO',
            'accesousu':'SINCLAVE',
            'accesobod':'SINCLAVE',
            'accesocos':'SINCLAVE'
        }
        

     return {
            # Si la sesión tiene acceso usa True, si no existe usa False por defecto
            'nombreusu': request.session.get('nombreusu', 'NINGUNO'),
            'accesousu': request.session.get('accesousu', 'SINCLAVE'),
            'accesobod': request.session.get('accesobod', 'SINCLAVE'),
            'accesocos': request.session.get('accesocos', 'SINCLAVE')
        }


