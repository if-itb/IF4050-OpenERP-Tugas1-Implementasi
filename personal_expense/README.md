![odoo logo](http://www.odoo.com/openerp_website/static/src/img/assets/png/odoo_logo_rgb.png)
# Personal-Expenses Odoo(openerp) addtional Module
**IF-4050 Experimental Module**


Personal_Expenses module is a simple module that enable users to note their expenses. This simple module is built over the openERP base module.

##Installation
Follow these steps in order to use this module. The steps are :
- Get the 'personal-expenses' module folder either by pulling it with git or download it as zip
- Move or copy the folder to your openerp server '/addons/' directory
- Try to 'update the module list' by clicking this button 
- search for 'personal expenses' module using the search form
- click 'install' button
- Now, you'll see **'personal expenses'** on your menubar

##Components Explanation

##Tech
Building this module we use the odoo.py feature (scaffold) to generate standards module template that completes :
- ```__init__.py```
- ```__openerp__.py```
- controllers.py
- demo.xml
- models.py
- security
- and templates.xml

> infact, we can modify the structure by editing the ```__openerp__.py``` file and ```__init__.py``` file.

###template generation
```
$ python odoo.py scaffold [name] [destination directory]
```
##Troubleshooting
It is likely to meet some trouble while installing or running modules. So far, We have found and overcome some :
- Cannot find the 'update module list' in installing the module
    >go to user management and check list 'technology access' button --> after this, go back and check out  for the 'update module list' button.

If any of you found another trouble and insight, we are pleased to know :)

_P.S : Mail us (contacts below)_

##Exploration (on-going)
**Communication with 'lunch' module**

we are trying to create communication with the lunch module, so when employees spend on lunch it will automaticly create a spending notes in personal expenses module.
Now, we are still struggling to figure the connection between these two modules by creating a model to bridge them.
### Version
0.1

The Team
----

- M Harya Putra 18211011@std.stei.itb.ac.id
- Andy Primawan 18211030@std.stei.itb.ac.id
- Christian Hendy 18211036@std.stei.itb.ac.id
- M Fatoni 18211042@std.stei.itb.ac.id
- Aria Dhanang 182110@std.stei.itb.ac.id

----
**GO GET GOLD**
