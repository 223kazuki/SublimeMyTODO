import sublime, sublime_plugin

class ListTodosCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('SimplestTodo.sublime-settings')
        TODO_STR = settings.get("todo_prefix")
        DONE_STR = settings.get("done_prefix")
        self.keys = []
        self.lines = []
        allContent = sublime.Region(0, self.view.size())
        regions = self.view.split_by_newlines(allContent)
        for r in enumerate(regions):
            line = self.view.substr(r[1])
            if TODO_STR in line:
                self.keys.append(line)
                self.lines.append(r)
        sublime.active_window().show_quick_panel(self.keys, self.goto)

    def goto(self, arrpos):
        if arrpos >= 0:
            target_region = self.lines[arrpos][1]
            target_line = self.view.substr(self.lines[arrpos][1])
            self.view.sel().clear()
            self.view.sel().add(target_region)
            self.view.show(self.lines[arrpos][1])
            sublime.active_window().run_command("toggle_todo")
            sublime.active_window().run_command("list_todos")

def toggle(s):
    settings = sublime.load_settings('SimplestTodo.sublime-settings')
    TODO_STR = settings.get("todo_prefix")
    DONE_STR = settings.get("done_prefix")
    if TODO_STR in s:
        return s.replace(TODO_STR, DONE_STR)
    else:
        return s.replace(DONE_STR, TODO_STR)

class ToggleTodoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        line = view.line(view.sel()[0])
        before = view.substr(line)
        after = toggle(before)
        view.replace(edit, line, after)

class NewTodoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('SimplestTodo.sublime-settings')
        TODO_STR = settings.get("todo_prefix")
        DONE_STR = settings.get("done_prefix")
        view = self.view
        line = view.line(view.sel()[0])
        before = view.substr(line)
        after = before + TODO_STR
        view.replace(edit, line, after)
        end = line.end() + len(TODO_STR)
        r = sublime.Region(end, end);
        self.view.sel().clear()
        self.view.sel().add(r)
