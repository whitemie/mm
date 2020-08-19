# -*- coding -*-
import yaml


def get_data(fnpath):
    with open(fnpath, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        andatas = datas["add"]["mynormaldatas"]
        anids = datas["add"]["mynormalids"]
        aedatas = datas["add"]["myexceptdatas"]
        dndatas = datas["div"]["mynormaldata"]
        dedatas = datas["div"]["myexceptdata"]
        sdatas = datas["sub"]
        mdatas = datas["mul"]
        return [andatas, anids, aedatas, dndatas, dedatas, sdatas, mdatas]
