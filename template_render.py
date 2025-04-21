from docxtpl import DocxTemplate


def render_template(template_path, context, output_path):
    """
    Renders a Word document template with the provided context.

    :param template_path: Path to the Word document template.
    :param context: Dictionary containing the context for rendering.
    :param output_path: Path to save the rendered document.
    """
    # Load the template
    doc = DocxTemplate(template_path)

    # Render the template with the context
    doc.render(context)

    # Save the rendered document
    doc.save(output_path)
