# -*- coding: utf-8 -*-

from wow_wtf_manager.models import api


def test():
    _ = api.Client
    _ = api.Account
    _ = api.Realm
    _ = api.Character


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.models.api", preview=False)
