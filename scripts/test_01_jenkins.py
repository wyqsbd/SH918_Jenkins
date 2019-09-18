import allure


class TestJen:

    @allure.step("添加测试步骤")
    def test_001(self):
        allure.attach("附件名称", "附件中的内容描述")
        assert True
