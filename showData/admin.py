from mptt.admin import DraggableMPTTAdmin
class FileAdmin(DraggableMPTTAdmin):
    mptt_ident_field = 'name'