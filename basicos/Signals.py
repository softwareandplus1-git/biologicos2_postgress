# mi_app/signals.py
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

# (Tu señal de login que ya armamos antes se queda igual...)

@receiver(user_logged_out)
def limpiar_valores_al_cerrar_sesion(sender, request, user, **kwargs):
    # Destruye la sesión actual por completo eliminando todas las variables personalizadas
    request.session.flush()
    request.session.modified = True
