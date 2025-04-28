c = get_config()  # noqa: F821
c.NbConvertApp.export_format = 'markdown'

c.TemplateExporter.exclude_input = True
c.TemplateExporter.exclude_input_prompt = True
c.ExecutePreprocessor.enabled = True
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags.add("hide")
# c.NbConvertApp.output_base='./out/{notebook_name}'
c.NbConvertApp.output_files_dir = 'img'
