from django.contrib import admin
from django.contrib import messages


class CampaignModelAdmin(admin.ModelAdmin):
    # --------------------------custom field-----------------------------
    # list_display = ('name', 'status', 'date_created', 'added_on')

    # ----------------------display column in table view-----------------
    list_display = ('name', 'serving_status', 'date_created')

    # ----------------searchable field----------------------------------
    search_fields = ["name"]

    # -----------------define which field should be sortable------------
    # sortable_by = ('name', 'status', 'added_on')

    # ----------------add filter option for a specific field------------
    list_filter = ["status", "name"]

    # -----------if custom field is added then a function should create with the same name------------------
    # def added_on(self, obj):
    #     return obj.date_created

    # ---------------make custom field sortable-------------------------------------
    # added_on.admin_order_field = 'date_created'


    def make_active(modeladmin, request, queryset):
        # ------add new action in the action dropdown----------------
        # queryset.update(is_active=1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        # ------add new action in the action dropdown----------------
        # queryset.update(is_active=0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")

    # ------ the custom actions are added here--------------------------
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")


class AppModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')


class AppUserModelAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'date_created')


class UserConversionEventModelAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'id', 'date_created')


class UserSubscriptionEventModelAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'id', 'date_created')


class OrganicUserDataModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created')


class BulkUserDataModelAdmin(admin.ModelAdmin):
    list_display = ('user_identifier', 'id', 'date_created')


class BulkAttributionDataModelAdmin(admin.ModelAdmin):
    list_display = ('user_identifier', 'id', 'date_created')


class MultiDBModelAdmin(admin.ModelAdmin):
    # common base model for multiple database management

    # A handy constant for the name of the alternate database.
    # using = "logo"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )
