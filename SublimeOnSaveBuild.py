import sublime, sublime_plugin

class SublimeOnSaveBuild( sublime_plugin.EventListener ):
    def on_post_save( self, view ):
    	ext = view.file_name().split('.')[len(view.file_name().split('.'))-1]
    	if ext in "styl coffee less".split(' '):
        	view.window().run_command( "build" )