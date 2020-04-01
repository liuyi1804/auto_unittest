from poium import Page, PageElement

class LoginPage(Page):

	account_input = PageElement(xpath="//*[@class='el-input__inner' and @type='text']")
	passwd_input = PageElement(xpath="//*[@class='el-input__inner' and @type='password']")
	login_button = PageElement(xpath="//*[@class='el-button el-button--primary el-button--large']")