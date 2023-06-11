# -*- coding: utf-8 -*-

from wow_wtf_manager.models.acc_realm_char import (
    Account,
    Realm,
    Character,
)


class Test:
    acc1 = Account.new("acc1")
    acc2 = Account.new("acc2")

    realm1_1 = Realm.new(acc1, "realm1")
    realm1_2 = Realm.new(acc1, "realm2")
    realm2_1 = Realm.new(acc2, "realm1")
    realm2_2 = Realm.new(acc2, "realm2")

    char1_1_1 = Character.new(realm1_1, "char1")
    char1_1_2 = Character.new(realm1_1, "char2")
    char1_2_1 = Character.new(realm1_2, "char1")
    char1_2_2 = Character.new(realm1_2, "char2")
    char2_1_1 = Character.new(realm2_1, "char1")
    char2_1_2 = Character.new(realm2_1, "char2")
    char2_2_1 = Character.new(realm2_2, "char1")
    char2_2_2 = Character.new(realm2_2, "char2")

    def test_hash_and_comparison(self):
        st = {self.acc1, self.acc2, self.acc1, self.acc2}
        assert len(st) == 2
        assert self.acc1 < self.acc2
        assert self.acc1 == self.acc1
        assert self.acc1 != self.acc2

        st = {self.realm1_1, self.realm1_2, self.realm2_1, self.realm2_2}
        assert len(st) == 4
        st1 = st & st
        assert len(st1) == 4
        assert self.realm1_1 < self.realm1_2
        assert self.realm1_1 == self.realm1_1
        assert self.realm1_1 != self.realm1_2

        st = {
            self.char1_1_1,
            self.char1_1_2,
            self.char1_2_1,
            self.char1_2_2,
            self.char2_1_1,
            self.char2_1_2,
            self.char2_2_1,
            self.char2_2_2,
        }
        assert len(st) == 8
        st1 = st & st
        assert len(st1) == 8
        assert self.char1_1_1 < self.char1_1_2
        assert self.char1_1_1 == self.char1_1_1
        assert self.char1_1_1 != self.char1_1_2

    def test_attributes(self):
        assert len(self.acc1.sort_key) == 20
        assert len(self.acc1.realms_mapper) == 2
        assert self.acc1.realms == [self.realm1_1, self.realm1_2]
        assert len(self.acc1.characters) == 4
        assert self.acc1.capitalized_account_name == "ACC1"

        assert len(self.realm1_1.sort_key) == 41
        assert len(self.realm1_1.characters_mapper) == 2
        assert self.realm1_1.account_name == self.acc1.account
        assert self.realm1_1.characters == [self.char1_1_1, self.char1_1_2]

        assert len(self.char1_1_1.sort_key) == 62
        assert self.char1_1_1.account_name == self.acc1.account
        assert self.char1_1_1.realm_name == self.realm1_1.realm
        assert self.char1_1_1.titled_character_name == "Char1"


if __name__ == "__main__":
    from wow_wtf_manager.tests import run_cov_test

    run_cov_test(__file__, "wow_wtf_manager.models.acc_realm_char", preview=False)
