import frappe
import json

def setup_blog_desktop_icon():
    icon_name = "Blog"
    icon_data = {
        "label": "Blog",
        "icon": "pen",
        "icon_type": "Link",
        "link_type": "Workspace",
        "link_to": "Blog",
        "parent_icon": "",
        "hidden": 0,
        "standard": 1,
        "app": "blog",
        "idx": 25
    }

    if frappe.db.exists("Desktop Icon", icon_name):
        frappe.db.set_value("Desktop Icon", icon_name, icon_data)
    else:
        doc = frappe.new_doc("Desktop Icon")
        doc.name = icon_name
        doc.update(icon_data)
        doc.insert(ignore_permissions=True)

    if frappe.db.table_exists("Desktop Layout"):
        layouts = frappe.get_all("Desktop Layout", fields=["name", "layout"])
        for l in layouts:
            if not l.layout:
                continue
            try:
                items = json.loads(l.layout)
                has_it = any(x.get("name") == icon_name or x.get("label") == icon_name for x in items)
                if not has_it:
                    c_item = {
                        "label": "Blog",
                        "bg_color": "blue",
                        "link": None,
                        "link_type": "Workspace",
                        "app": "blog",
                        "icon_type": "Link",
                        "parent_icon": "",
                        "icon": "pen",
                        "link_to": "Blog",
                        "idx": 25,
                        "standard": 1,
                        "logo_url": None,
                        "hidden": 0,
                        "name": "Blog",
                        "restrict_removal": 0,
                        "icon_image": None
                    }
                    items.append(c_item)
                    doc_l = frappe.get_doc("Desktop Layout", l.name)
                    doc_l.layout = json.dumps(items)
                    doc_l.save(ignore_permissions=True)
            except Exception:
                pass

def after_install():
    setup_blog_desktop_icon()
    frappe.db.commit()

def after_migrate():
    setup_blog_desktop_icon()
    frappe.db.commit()
