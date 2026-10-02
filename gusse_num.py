scrt_num=25

while True:
   let=int(input("gusses the number : "))
   if let==scrt_num:
    print("gusses is correct")
    break

   elif let > scrt_num:
      print("gusses is high")
   elif let < scrt_num:
      print("gusses is low")        