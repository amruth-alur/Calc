Window.size = (1920,1080)

class NR(MDApp, App):
    DEBUG = 0
    KV_FILES = {
        os.path.join(os.getcwd(), "screenmanager.kv"),
        os.path.join(os.getcwd(), "FirstPage.kv"),  
	@@ -27,4 +27,6 @@ def build_app(self):
    LabelBase.register(name="SPoppins", fn_regular="Poppins-Regular.ttf")
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Bold.ttf")
    LabelBase.register(name="LPoppins", fn_regular="Poppins-Light.ttf")
    LabelBase.register(name="SpaceMonoB", fn_regular="SpaceMono-Bold.ttf")
    LabelBase.register(name="SpaceMonoR", fn_regular="SpaceMono-Regular.ttf")
    NR().run()
