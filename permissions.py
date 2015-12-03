# admin
from django.contrib import admin


class DeleteOnly(admin.ModelAdmin):
    # Overrides
    def save_model(self, request, obj, form, change):
        pass
    
    # Permissions
    def has_add_permission(self, request, obj=None):
        return False
    
    # Templates
    change_form_template = 'admin_tools/view_form.html'



class DisableDelete(admin.ModelAdmin):
    # Action Options
    def get_actions(self, request):
        actions = super(DisableDelete, self).get_actions(request)
        del actions['delete_selected']
        return actions
        
    # Permissions
    def has_delete_permission(self, request, obj=None):
        return False



class ChangeOnly(admin.ModelAdmin):
    # Action Options
    def get_actions(self, request):
        actions = super(ChangeOnly, self).get_actions(request)
        del actions['delete_selected']
        return actions
        
    # Permissions
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



''' NOTE: Read-Only fields must be defined in child classes.
      ex: readonly_fields = MODEL_NAME._meta.get_all_field_names()
'''
class ViewOnly(admin.ModelAdmin):
    # Action Options
    def get_actions(self, request):
        actions = super(ViewOnly, self).get_actions(request)
        del actions['delete_selected']
        return actions

    # Overrides
    def save_model(self, request, obj, form, change):
        pass

    # Permissions
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    # Templates
    change_form_template = 'admin_tools/view_form.html'
