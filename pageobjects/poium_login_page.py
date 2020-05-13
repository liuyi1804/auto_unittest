from poium import Page, PageElement
import sys
# 继承基类之前把对应目录加入path
sys.path.append("../framework/")
from framework.base_page import BasePage

class LoginPage(BasePage):

	account_input = PageElement(xpath="//*[@class='el-input__inner' and @type='text']")
	password_input = PageElement(xpath="//*[@class='el-input__inner' and @type='password']")
	login_button = PageElement(xpath="//*[@class='el-button el-button--primary el-button--large']")