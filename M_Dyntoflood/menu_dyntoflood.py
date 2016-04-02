bl_info = {
    "name": "Menu Dynto Flood",
    "author": "Jose Antonio Garcia Sanchez",
    "version": (0, 0, 1),
    "blender": (2, 72, 0),
    "location": "View3D",
    "description": "Manejo de valor",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "",
    "category": "menu",
}

import bpy


class MenuDynto(bpy.types.Menu):
    bl_label = "Dynto Flood"
    bl_idname = "Menu_flotante"

    def draw(self, context):
        wm = context.window_manager
        layout = self.layout

        layout.prop(wm, "flood_meshsculpt", "Flood Value")



def register():
    bpy.utils.register_class(MenuDynto)


def unregister():
    bpy.utils.unregister_class(MenuDynto)


if __name__ == "__main__":
    register()


    bpy.ops.wm.call_menu(name=Menu_flotante)
