from django import template

register = template.Library()

ICONOS_CATEGORIA = {
    'cyber': '🔐',
    'osint': '🔎',
    'pentesting': '⚔️',
    'red-team': '🎯',
    'blue-team': '🛡️',
    'defensa': '🛡️',
    'iso27001': '📜',
    'ens': '🏛️',
    'nist': '📐',
    'auditoria': '🔍',
    'grc': '📋',
    'riesgos': '⚠️',
    'privacidad': '🔒',
    'forense': '🧬',
    'web': '🌐',
    'python': '🐍',
    'desarrollo': '💻',
    'ia': '🧠',
    'laboratorio': '🧪',
    'auditsym': '🛠️',
    'devops': '🐳',
    'redes': '🌐',
    'code': '✨',
}

@register.filter
def categoria_icono(slug):
    return ICONOS_CATEGORIA.get(slug, '◈')