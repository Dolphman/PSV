import psv
import unittest

csv = """Name,Price,Available,Company
Product 1,10,1,Yahoo
Product 2,15,0,Microsoft
Product 3,1,1,Google
Product 4,20,0,Yahoo
Product 5,25,1,Yahoo
Product 6,30,1,Google
Product 7,10,0,Yahoo
"""

csv_repeat = """Name,Price,Available,Company
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
Product 1,10,1,Yahoo
"""

csv_empty = """Name,Price,Available,Company
,,,
,,,
,,,
,,,
,,,
,,,
,,,
"""


special = "TEST,test,TEst"
    
csv_row_obj = """ROW_OBJ,TEST
TEST,TEST"""


class psv_selections_test(unittest.TestCase):

    def construct(self):
        self.csvdoc = psv.loads(csv)

    def test_delete_rows(self):
        self.construct()
        try:
            del self.csvdoc.rows[0]
        except Exception as err:
            self.fail(err)

    def test_delete_rows_deleter(self):
        self.construct()
        try:
            del self.csvdoc[0]
        except Exception as err:
            self.fail(err)

    def test_delete_rows_getitem(self):
        self.construct()
        try:
            del self.csvdoc[0]
        except Exception as err:
            self.fail(err)

    def test_select_accepts_func(self):
        self.construct()
        try:
            self.csvdoc.select(lambda x: True)
        except Exception as err:
            self.fail(str(err))

    def test_select_function_generation(self):
        self.construct()
        try:
            self.csvdoc.select("name")
            self.csvdoc.select(name="Product 1")
            self.csvdoc.select("name", price=10)
            self.csvdoc.select("name", price=lambda p: p > 10)
            self.csvdoc.select("name", price=10, company="Yahoo", available=1)
        except Exception as err:
            self.fail(str(err))

    def test_any_select_function_generation(self):
        self.construct()
        try:
            self.csvdoc.any("name")
            self.csvdoc.any(name="Product 1")
            self.csvdoc.any("name", price=10)
            self.csvdoc.any("name", price=lambda p: p > 10)
            self.csvdoc.any("name", price=10, company="Yahoo", available=1)
        except Exception as err:
            self.fail(str(err))

    def test_select_function_generation_results(self):
        self.construct()
        self.assertEqual(len(self.csvdoc.select("name")), 7)
        self.assertEqual(len(self.csvdoc.select(lambda x: x.name)), 7)
        self.assertEqual(len(self.csvdoc.select(name="Product 1")), 1)
        self.assertEqual(len(self.csvdoc.select("name", price=10)), 2)
        self.assertEqual(len(self.csvdoc.select(lambda x: x.name, price=10)), 2)
        self.assertEqual(len(self.csvdoc.select("name", price=lambda p: p > 10)), 4)
        self.assertEqual(len(self.csvdoc.select(lambda x: x.name, price=lambda p: p > 10)), 4)
        self.assertEqual(len(self.csvdoc.select("name", price=10, company="Yahoo", available=1)), 1)
    
    def test_any_select_function_generation_results(self):
        self.construct()
        self.assertEqual(len(self.csvdoc.any("name")), 7)
        self.assertEqual(len(self.csvdoc.any(lambda x: x.name)), 7)
        self.assertEqual(len(self.csvdoc.any(name="Product 1")), 1)
        self.assertEqual(len(self.csvdoc.any("name", price=10)), 7)
        self.assertEqual(len(self.csvdoc.any(lambda x: x.name, price=10)), 7)
        self.assertEqual(len(self.csvdoc.any("name", price=lambda p: p > 10)), 7)
        self.assertEqual(len(self.csvdoc.any(lambda x: x.name, price=lambda p: p > 10)), 7)
        self.assertEqual(len(self.csvdoc.any("name", price=10, company="Yahoo", available=1)), 7)


    def test_safe_select_accepts_func(self):
        self.construct()
        try:
            self.csvdoc.safe_select(lambda x: True)
        except Exception as err:
            self.fail(str(err))

    def test_safe_select_function_generation(self):
        self.construct()
        try:
            self.csvdoc.safe_select()
            self.csvdoc.safe_select("name")
            self.csvdoc.safe_select(name="Product 1")
            self.csvdoc.safe_select("name", price=10)
            self.csvdoc.safe_select("name", price=lambda p: p > 10)
            self.csvdoc.safe_select("name", price=10, company="Yahoo", available=1)
        except Exception as err:
            self.fail(str(err))

    def test_any_safe_select_function_generation(self):
        self.construct()
        try:
            self.csvdoc.safe_any()
            self.csvdoc.safe_any("name")
            self.csvdoc.safe_any(name="Product 1")
            self.csvdoc.safe_any("name", price=10)
            self.csvdoc.safe_any("name", price=lambda p: p > 10)
            self.csvdoc.safe_any("name", price=10, company="Yahoo", available=1)
        except Exception as err:
            self.fail(str(err))


    def test_safe_select_function_generation_results(self):
        self.construct()
        self.assertEqual(len(self.csvdoc.safe_select("name")), 7)
        self.assertEqual(len(self.csvdoc.safe_select(lambda x: x.name)), 7)
        self.assertEqual(len(self.csvdoc.safe_select(name="Product 1")), 1)
        self.assertEqual(len(self.csvdoc.safe_select("name", price=10)), 2)
        self.assertEqual(len(self.csvdoc.safe_select(lambda x: x.name, price=10)), 2)
        self.assertEqual(len(self.csvdoc.safe_select("name", price=lambda p: p > 10)), 4)
        self.assertEqual(len(self.csvdoc.safe_select(lambda x: x.name, price=lambda p: p > 10)), 4)
        self.assertEqual(len(self.csvdoc.safe_select("name", price=10, company="Yahoo", available=1)), 1)        


    def test_any_safe_select_function_generation_results(self):
        self.construct()
        self.assertEqual(len(self.csvdoc.safe_any("name")), 7)
        self.assertEqual(len(self.csvdoc.safe_any(lambda x: x.name)), 7)
        self.assertEqual(len(self.csvdoc.safe_any(name="Product 1")), 1)
        self.assertEqual(len(self.csvdoc.safe_any("name", price=10)), 7)
        self.assertEqual(len(self.csvdoc.safe_any(lambda x: x.name, price=10)), 7)
        self.assertEqual(len(self.csvdoc.safe_any("name", price=lambda p: p > 10)), 7)
        self.assertEqual(len(self.csvdoc.safe_any(lambda x: x.name, price=lambda p: p > 10)), 7)
        self.assertEqual(len(self.csvdoc.safe_any("name", price=10, company="Yahoo", available=1)), 7)

    def test_no_output(self):
        self.construct()
        self.csvdoc.no_output()
        self.assertEqual(self.csvdoc.lenoutput(), 0)

    def test_all_output(self):
        self.construct()
        self.csvdoc.no_output()
        self.csvdoc.all_output()
        self.assertEqual(self.csvdoc.lenoutput(), 7)

    def test_flip_output(self):
        self.construct()
        self.csvdoc[:3].no_output()
        self.csvdoc.flip_output()
        self.assertEqual(self.csvdoc.lenoutput(), 3)

    def test_lenoutput(self):
        self.construct()
        try:
            self.csvdoc.lenoutput()
        except Exception as err:
            self.fail(str(err))

    def test_len_no_output(self):
        self.construct()
        try:
            self.csvdoc.lenoutput()
        except Exception as err:
            self.fail(str(err))

    def test_columns(self):
        self.construct()
        try:
            self.csvdoc.columns
        except Exception as err:
            self.fail(str(err))

    def test_enable(self):
        self.construct()
        self.csvdoc.no_output()
        self.csvdoc.enable(name="Product 1")
        self.assertEqual(self.csvdoc.lenoutput(), 1)

    def test_disable(self):
        self.construct()
        self.csvdoc.disable(name="Product 1")
        self.assertEqual(self.csvdoc.lenoutput(), 6)

    def test_flip(self):
        self.construct()
        self.csvdoc.flip(name="Product 1")
        self.assertEqual(self.csvdoc.lenoutput(), 6)

    def test_grab(self):
        self.construct()
        self.assertEqual(tuple(self.csvdoc["name"]), self.csvdoc.grab("name"))
        self.assertEqual(tuple(self.csvdoc["name", "price"]), self.csvdoc.grab("name", "price"))

    def test_unique(self):
        self.construct()
        self.assertEqual(set(self.csvdoc["name"]), self.csvdoc.unique("name"))
        self.assertEqual(set(self.csvdoc["name", "price"]), self.csvdoc.unique("name", "price"))

    def test_indexing(self):
        self.construct()
        self.assertTrue(isinstance(self.csvdoc.grab("name", "ROW_OBJ")[0][1], psv.core.objects.rowobjects.BaseRow))
        try:
            self.csvdoc.grab("ROW_OBJ")
            self.csvdoc.fail("PSV did not catch incorrect ROW_OBJ use")
        except:
            pass

        self.assertTrue(isinstance(self.csvdoc[0],  psv.core.objects.rowobjects.BaseRow))

    def test_tabulating(self):
        self.construct()
        try:
            self.csvdoc.tabulate()
            self.csvdoc.tabulate(format="html", limit=10, only_ascii=False, text_limit=1000, remove_newline=False)
        except Exception as err:
            self.fail(str(err))

    def test_find(self):
        self.construct()
        self.assertTrue(bool(self.csvdoc.find(name="Product 1")))
        self.assertFalse(bool(self.csvdoc.find(name="INVALID NAME")))

    def test_findall(self):
        self.construct()
        self.assertEqual(len(self.csvdoc.find_all(company="Yahoo")), 4)
        self.assertFalse(bool(self.csvdoc.find_all(company="INVALID COMPANY")))

    def test_single_find(self):
        self.construct()
        self.assertTrue(bool(self.csvdoc.single_find(name="Product 1")))
        self.assertFalse(bool(self.csvdoc.single_find(name="INVALID NAME")))
        try:
            self.csvdoc.find(company="Yahoo")
            self.fail("Single Find did not raise exception for duplicates")
        except Exception:
            pass

    def test_merge(self):
        self.construct()
        try:
            self.csvdoc.merge(self.csvdoc[:int(len(self.csvdoc)/2)])
        except Exception as err:
            self.fail(err)

    def test_merge_valueerror(self):
        self.construct()
        with self.assertRaises(ValueError) as cm:
            self.csvdoc.merge(psv.new())


    def test_safe_merge(self):
        self.construct()
        try:
            self.csvdoc.safe_merge(self.csvdoc[:int(len(self.csvdoc)/2)])
        except Exception as err:
            self.fail(err)


    def test_non_hash_merge(self):
        self.construct()
        try:
            self.csvdoc.non_hash_merge(self.csvdoc[:int(len(self.csvdoc)/2)])
        except Exception as err:
            self.fail(err)

    def test_columns_setterworks(self):
        self.construct()
        self.csvdoc.columns
        self.csvdoc.columns = ["Hello 5"]
    
    def test_addrow(self):
        self.construct()
        row = self.csvdoc.addrow()
        self.assertEqual(row, self.csvdoc[-1])

    def test_addcolumn(self):
        self.construct()
        self.csvdoc.addcolumn("Test-Row-1")
        print(self.csvdoc.columns)
        self.assertTrue("Test-Row-1" in self.csvdoc.columns)
        self.assertTrue("testrow1" in self.csvdoc.__columnsmap__.keys())

 
    def test_delcolumn(self):
        self.construct()
        self.csvdoc.addcolumn("Test-Row-1") #This is covered in seperate test
        self.csvdoc.delcolumn("Test-Row-1")
        self.assertFalse("Test-Row-1" in self.csvdoc.columns)
        self.assertFalse("testrow1" in self.csvdoc.__columnsmap__.keys())

    def test_addrow_kw(self):
        import random
        self.construct()
        row = self.csvdoc.addrow(**({x:random.randint(1,100) for x in self.csvdoc.columns} ))
        self.assertEqual(row, self.csvdoc[-1])

    def test__columnsmap__(self):
        self.construct()
        try:
            self.csvdoc.__columnsmap__
        except Exception as err:
            self.fail(str(err))

    def test__columnsmap___select(self):
        self.construct()
        try:
            self.csvdoc.select().__columnsmap__
        except Exception as err:
            self.fail(str(err))

    def test_repeat_columns(self):
        try:
            api = psv.loads(special)
        except Exception as err:
            self.fail(str(err))

    def test_badgetitem_main(self):
        self.construct()
        with self.assertRaises(TypeError) as cm:
            self.csvdoc[None]


    def test_badgetitem_select(self):
        self.construct()
        with self.assertRaises(TypeError) as cm:
            self.csvdoc.select()[None]


    def test_addcolumn_failure(self):
        TEST = psv.new("TEST")
        with self.assertRaises(ValueError) as cm:
            TEST.addcolumn("TEST")      

    def test_utils_multiindex(self):
        test = psv.loads(csv_row_obj)
        value = test.grab("|ROW_OBJ|", "ROW_OBJ")
        self.assertTrue(isinstance(value[0][0], str))
        self.assertTrue(isinstance(value[0][1], psv.core.objects.rowobjects.BaseRow))

    def test_multiindex_typeerror(self):
        self.construct()
        with self.assertRaises(TypeError) as cm:
            self.csvdoc.grab(False, None)

    def test_badgrab_valueerror(self):
        self.construct()
        with self.assertRaises(ValueError) as cm:
            self.csvdoc.grab(*tuple())

    def test_remove_duplicates(self):
        test = psv.loads(csv_repeat)
        try:
            test = test.remove_duplicates()
        except Exception as err:
            self.fail(str(err))
        self.assertEqual(len(test), 1)

    def test_remove_duplicates_hard(self):
        test = psv.loads(csv_repeat)
        try:
            test.remove_duplicates(soft=False)
        except Exception as err:
            self.fail(str(err))
        self.assertEqual(len(test), 1)


    def test_arg_select(self):
        test = psv.loads(csv_empty)
        try:
            self.assertEqual(len(test.select("Name")),0)
        except Exception as exc:
            self.fail(str(exc))

    # def test_select_typeerror(self):
    #     self.construct()
    #     with self.assertRaises(TypeError) as cm:
    #         self.csvdoc.select(tuple())

    # def test_anyselect_typeerror(self):
    #     self.construct()
    #     with self.assertRaises(TypeError) as cm:
    #         self.csvdoc.any(tuple())