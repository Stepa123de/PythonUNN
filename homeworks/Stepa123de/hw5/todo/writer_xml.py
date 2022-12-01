import xml.etree.ElementTree as ET

from loguru import logger


def _remove_enter(string: str) -> str:
    return string.replace('\n', '')


def _append_elem(root, string: str, text: str = None):
    name = ET.Element(string)
    if text is not None:
        name.text = text
    root.append(name)


def _append_type_info(string: str, user_info: dict, root):
    names = ET.Element(string)

    for user_post in user_info.get(string):
        name = ET.Element(string[:-1])
        names.append(name)
        _append_elem(name, 'id', str(user_post.get('id')))
        _append_elem(name, 'title', _remove_enter(str(user_post.get('title'))))

        match string:
            case 'posts':
                body = _remove_enter(str(user_post.get('body')))
                _append_elem(name, 'body', body)
            case 'todos':
                completed = _remove_enter(str(user_post.get('completed')))
                _append_elem(name, 'completed', completed)
    root.append(names)


def write_xml(user_id: str, user_email: str, user_info: dict, types_info: list, path: str):
    root = ET.Element('user')
    _append_elem(root, 'id', user_id)
    _append_elem(root, 'email', user_email)
    for type_info in types_info:
        _append_type_info(type_info, user_info, root)

    etree = ET.ElementTree(root)
    ET.indent(etree)
    with open(path, 'wb') as xml_file:
        etree.write(xml_file, encoding='utf-8', xml_declaration=True)

    logger.info('Saved {0}/{1}.xml for user with email `{2}`'.format(
        path,
        user_id,
        user_email,
    ))
