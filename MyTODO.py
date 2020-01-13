import sublime
import sublime_plugin

TODO_STR = "□"
TODO_DONE_STR = "☑"

class MyTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.edit = edit
		self.keys = []
		allContent = sublime.Region(0, self.view.size())
		self.regions = self.view.split_by_newlines(allContent)

		self.lines = []
		
		for r in enumerate(self.regions):
			line = self.view.substr(r[1])
			if TODO_STR in line:
				self.keys.append(line)
				self.lines.append(r)
		sublime.active_window().show_quick_panel(self.keys, self.goto)

	def goto(self, arrpos):
		if arrpos >= 0:
			target_region = self.lines[arrpos][1]
			target_line = self.view.substr(self.lines[arrpos][1])
			# self.view.replace(self.edit, target_region, 'REPLACE!')
			print(self.lines[arrpos][1])
			self.view.sel().clear()
			self.view.sel().add(target_region)
			self.view.show(self.lines[arrpos][1])
