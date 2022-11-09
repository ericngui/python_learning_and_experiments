import re 
  def rearrange_name(name):
    ## Define what character that is intended to be matched with
     result = re.search(r"^([\w -]+), ([\w. ]+)$", name)
     if result is None:
         return name
      ## Formatting the print return result by first name and last name
     return "{} {}".format(result[2], result[1])

>>> rearrange_name("Inugami, Korone")
'Korone Inugami'
>>> rearrange_name("Nekomata, Okayu")
'Okayu Nekomata'
>>> rearrange_name("van der Sar, Edwin")
'Edwin van der Sar'
>>> rearrange_name("Vennegoor of Hesselink, Jan")
'Jan Vennegoor of Hesselink'
