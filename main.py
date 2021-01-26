from ieLib import IE

ie = IE(visible=True)

ie.navigate('xxx')
ie.get_elements_by_name('username')[1].value = 'xxx'
ie.get_elements_by_name('password')[0].value = 'xxx'
ie.get_elements_by_class_name('btn btn-large btn-inverse btn-block')[0].click()
ie.wait_its_ready()

#14a86fbc0091
