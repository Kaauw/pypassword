# pypassword module

Simple python module to generate password using secrets library

## Usage

```python

>>> from pypassword import Password
>>> pw = Password(20)
>>> pw.getpass()
>>> pw.generate()
>>> pw.getpass()
{'plain_text': '*1U9hn,IvTR4Gde*by1A', 'md5': 'c01cb2c7b7af662b3847e844c85cd730', 'sha256': '54be8dad97b08a8e4965119c97bd4ca3d21caa0b59a9a318429e8669f2d3c623'}
>>> pw.getpass_plain_text()
'*1U9hn,IvTR4Gde*by1A'
>>> pw.getpass_md5()
'c01cb2c7b7af662b3847e844c85cd730'
>>> pw.getpass_sha256()
'54be8dad97b08a8e4965119c97bd4ca3d21caa0b59a9a318429e8669f2d3c623'
>>> pw.getpass_sha512_crypt()
'$6$rounds=656000$FfWsWyv9/0X.Glez$Sr3HM54nZJcr.H..JVEsuL7DvNIWrQjBKqhMc7V8h/MP94lElCWPVrt4HqDK7kjaZF96VntwuaI1vPpyliMJC/'
```

## Unit tests
```bash
~\DevDir\pypassword> python .\test_pypassword.py
test_check_var_type (__main__.TestPassword)
Return true if type are correct ... ok
test_custom_lenght (__main__.TestPassword)
Return true if password lenght = 16 ... ok
test_default_car (__main__.TestPassword)
Return true if password lenght = 16 ... ok
test_get_md5 (__main__.TestPassword)
Return true if getpass_md5() is matching regex '^[0-9a-fA-F]{32}$' ... ok
test_get_sha256 (__main__.TestPassword)
Return true if getpass_sha256() is matching regex '^[A-Fa-f0-9]{64}$' ... ok
test_get_sha512_crypt (__main__.TestPassword)
Return true if getpass_sha512_crypt() is correctly encrypted ... ok

----------------------------------------------------------------------
Ran 6 tests in 1.645s

OK
```