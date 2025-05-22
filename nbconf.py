c = get_config()  # noqa: F821
c.NbConvertApp.export_format = 'markdown'

c.TemplateExporter.exclude_input = True
c.TemplateExporter.exclude_input_prompt = True
# c.TemplateExporter.exclude_output_prompt = True
c.ExecutePreprocessor.enabled = True
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags.add("hide")
c.TagRemovePreprocessor.remove_all_outputs_tags.add("tf")
# c.NbConvertApp.output_base='./out/{notebook_name}'
c.NbConvertApp.output_files_dir = 'img'

# c.Exporter.preprocessors = [
#     'nbconvert.preprocessors.ExecutePreprocessor',
#     'nbconvert.preprocessors.TagRemovePreprocessor'
#     # Add other preprocessors here if needed, in desired order
# ]