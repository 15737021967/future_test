
class MediaType:
    application_json = "application/json"
    application_xml = "application/xml"
    application_form = "application/x-www-form-urlencoded"
    multi_part = "multipart/form-data"
    text_plain = "text/plain; charset={charset}"
    text_html = "text/html"
    application_pdf = "application/pdf"
    image_png = "image/png"
    application_custom_vnd_template = "application/vnd.{custom_format}"
    custom_content_custom_vnd_template = "{custom_content}/vnd.{custom_format}"
