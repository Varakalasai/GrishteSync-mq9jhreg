# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import gradio as gr
from gradio import Blocks

# Define the Kanban board
boards = ['To-Do', 'In Progress', 'Done']

# Define the tasks
tasks = {
    'To-Do': ['Task 1', 'Task 2', 'Task 3'],
    'In Progress': ['Task 4', 'Task 5'],
    'Done': ['Task 6']
}

demo = gr.Blocks()

todo = gr.Column([
    gr.Markdown("### To-Do"),
    gr.Button("Move to In Progress"),
    gr.Textbox(label="Add Task")
])

in_progress = gr.Column([
    gr.Markdown("### In Progress"),
    gr.Button("Move to Done"),
    gr.Button("Move to To-Do")
])

done = gr.Column([
    gr.Markdown("### Done"),
    gr.Button("Move to In Progress")
])

demo.append(todo)
demo.append(in_progress)
demo.append(done)

demo.launch(server_name='0.0.0.0', server_port=7860)
print('Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com')