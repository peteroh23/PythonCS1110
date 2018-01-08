"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Junghwan Oh - jo299
Magd Bayoumi - mb2363
THE DATE COMPLETED HEREq
"""


import cornell
import a1

def testA():
	"test procedure for part A"
	#Test for '0.838095 Euros'
	cornell.assert_equals('0.838095', a1.before_space('0.838095 Euros'))
	cornell.assert_equals('Euros', a1.after_space('0.838095 Euros'))

	#Test for '5 Saudi Riyals'
	cornell.assert_equals('5', a1.before_space('5 Saudi Riyals'))
	cornell.assert_equals('Saudi Riyals', a1.after_space('5 Saudi Riyals'))

	#Test for ' 5'
	cornell.assert_equals('', a1.before_space(' 5'))
	cornell.assert_equals('5', a1.after_space(' 5'))

	#Test for '5 ' 
	cornell.assert_equals('5', a1.before_space('5 '))
	cornell.assert_equals('', a1.after_space('5 '))

	#Test for 'Peter Oh likes Tennis'
	cornell.assert_equals('Peter', a1.before_space('Peter Oh likes Tennis'))
	cornell.assert_equals('Oh likes Tennis', a1.after_space('Peter Oh likes Tennis'))

def testB():
	"test procedure for part B"
	
	#Test for first_inside_quotes
	cornell.assert_equals('C', a1.first_inside_quotes('A   B   "C"    D'))
	cornell.assert_equals('D   E   F', a1.first_inside_quotes('A    B    C    "D   E   F"'))
	cornell.assert_equals('   ', a1.first_inside_quotes('ABC "   " DEF'))

	#Test for get_lhs
	cornell.assert_equals('2 United States Dollars', a1.get_lhs('{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'))
	cornell.assert_equals('2.5 United States Dollars', a1.get_lhs('{ "success" : true, "lhs" : "2.5 United States Dollars", "rhs" : "2.0952375 Euros", "error" : "" }'))
	cornell.assert_equals('30000 United States Dollars', a1.get_lhs('{ "success" : true, "lhs" : "30000 United States Dollars", "rhs" : "6.5237409 Bitcoins", "error" : "" }'))


	#Test for get_rhs
	cornell.assert_equals('112518 Saudi Riyals', a1.get_rhs('{ "success" : true, "lhs" : "30000 United States Dollars", "rhs" : "112518 Saudi Riyals", "error" : "" }'))
	cornell.assert_equals('2384.8473112096 Saudi Riyals', a1.get_rhs('{ "success" : true, "lhs" : "30000 Dominican Pesos", "rhs" : "2384.8473112096 Saudi Riyals", "error" : "" }'))
	cornell.assert_equals('4975.8459973372 Hong Kong Dollars', a1.get_rhs('{ "success" : true, "lhs" : "30000 Dominican Pesos", "rhs" : "4975.8459973372 Hong Kong Dollars", "error" : "" }'))


	#Test for has_error
	cornell.assert_equals(True, a1.has_error('{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}'))
	cornell.assert_equals(False, a1.has_error('{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'))
	


def testC():
	"test procedure for part C"
	

	#Test for Currency Response
	cornell.assert_equals('{ "success" : true, "lhs" : "30000 United States Dollars", "rhs" : "112518 Saudi Riyals", "error" : "" }', a1.currency_response('USD', 'SAR', 30000))
	cornell.assert_equals('{ "success" : true, "lhs" : "2 United States Dollars", "rhs" : "1.67619 Euros", "error" : "" }', a1.currency_response('USD', 'EUR', 2))
	cornell.assert_equals('{ "success" : true, "lhs" : "0 Dominican Pesos", "rhs" : "0 Saudi Riyals", "error" : "" }', a1.currency_response('DOP', 'SAR', 0.0))



def testD():
	"test procedure for part D"
	


	# Test is_currency
	cornell.assert_equals(True, a1.iscurrency('USD'))
	cornell.assert_equals(True, a1.iscurrency('SAR'))
	cornell.assert_equals(False, a1.iscurrency('   '))
	cornell.assert_equals(False, a1.iscurrency('sar'))

	#Test Exchange
	cornell.assert_floats_equal(112.518, a1.exchange('USD', 'SAR', 30))





testA()
testB()
testC()
testD()


print("Module a1 passed all tests")





















