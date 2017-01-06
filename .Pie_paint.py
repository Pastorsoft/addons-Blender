bl_info = {
    "name": "Pie_Menus_Paint",
    "author": "Jose Ant. Garcia S",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "description": "Custom Pie Menus",
    "category": "3D View",}

import bpy
from bpy.types import Menu


class PieSculptPie(Menu):
    bl_idname = "pie.brochas"
    bl_label = "Brochas Paint"
    def poll(cls, context):
        settings = cls.paint_settings(context)
        return (settings and settings.brush and context.image_paint_object)

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()



        brush = context.tool_settings.image_paint.brush


        row = box.split(align=True)
        row.operator("image.save_dirty", text="Save All Images")

        box = pie.split().column()
        row = box.split(align=True)
        row.prop(brush, "mask_texture", new="texture.new", rows=3, cols=8)
        brush_mask_texture_settings(col, brush)



class PieSculpttres(Menu):
    bl_idname = "pie.paint"
    bl_label = "Options Paint"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        paint = context.tool_settings.image_paint

        box = pie.split().column()
        row = box.split(align=True)
        row.operator("image.save_dirty", text="Save All Images")
        #6 - Right
        box = pie.split().column()
        row = box.split(align=True)
        row.operator_menu_enum("paint.add_texture_paint_slot", "type")
        #2 - Bottom
        col = pie.column(align=True)
        col.operator("paint.brush_select", text="Draw", icon='BRUSH_TEXDRAW').texture_paint_tool='DRAW'
        col.operator("paint.brush_select", text='Mask', icon='BRUSH_TEXMASK').texture_paint_tool='MASK'
        col.operator("paint.brush_select", text='Clone', icon='BRUSH_CLONE').texture_paint_tool='CLONE'
        col.operator("paint.brush_select", text='Soften', icon='BRUSH_SOFTEN').texture_paint_tool='SOFTEN'
        col.operator("paint.brush_select", text="Fill", icon='BRUSH_TEXFILL').texture_paint_tool='FILL'
        col.operator("paint.brush_select", text='Smear', icon='BRUSH_SMEAR').texture_paint_tool='SMEAR'
        #8 - Top
        toolsettings = context.tool_settings
        ups = toolsettings.unified_paint_settings
        brush = toolsettings.sculpt.brush
        paintbrush = toolsettings.image_paint.brush
        col = pie.column(align=True)
        
        col.template_color_picker(brush, "color", value_slider=True)
        col.prop(ups, "size", text="Radius", slider=False)
        col.prop(paintbrush, "strength", slider=True)
        col.prop(paintbrush, "color",text="")
        col.prop(paintbrush, "secondary_color", text="")
        # - Top Left
        box = pie.split().column()
        row = box.split(align=True)
        row.label(text="Symmetry:")
        row = box.row(align=True)
        row = box.split(align=True)
        row.prop(paint, "use_symmetry_x", text="X", toggle=True)
        row.prop(paint, "use_symmetry_y", text="Y", toggle=True)
        row.prop(paint, "use_symmetry_z", text="Z", toggle=True)
        row = box.split(align=True)
        row.prop(paintbrush, "use_smooth_stroke")
        row = box.split(align=True)
        sub = box.row()
        sub.active = brush.use_smooth_stroke
        row.prop(paintbrush, "smooth_stroke_radius", text="Radius", slider=True)
        row = box.split(align=True)
        row.prop(paintbrush, "smooth_stroke_factor", text="Factor", slider=True)
        #7 - Top Right
        col = pie.column(align=True)
        col.prop(paintbrush, "stroke_method", text="", icon='IPO_CONSTANT')
        col.prop(paintbrush, "spacing", slider=True)
        col.prop(paintbrush,"jitter", slider=True)
        #9 - Bottom Left
        col = pie.column(align=True)
        col.prop(paintbrush, "blend", text="Blend")
        col.prop(paintbrush, "use_accumulate")
        col.prop(paintbrush, "use_alpha")
        col.prop(paintbrush, "use_gradient")
            # - Bottom Right


addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)

    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:


        km = wm.keyconfigs.addon.keymaps.new(name='Image Paint')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS')
        kmi.properties.name = "pie.brochas"


        km = wm.keyconfigs.addon.keymaps.new(name='Image Paint')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
        kmi.properties.name = "pie.paint"


def unregister():
    bpy.utils.unregister_module(__name__)


    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        for km in addon_keymaps:
            for kmi in km.keymap_items:
                km.keymap_items.remove(kmi)

            wm.keyconfigs.addon.keymaps.remove(km)


    del addon_keymaps[:]

if __name__ == "__main__":
    register()
