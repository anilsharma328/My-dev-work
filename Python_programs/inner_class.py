class outer:
     def __init__(self):
         print("this is outer class")

     class inner:
          def __init__(self):
              print("this is inner class")
          class inner_inner:
              def __init__(self):
                  print("this is inner_inner class")

outer_class_obj=outer()
inner_class_obj=outer_class_obj.inner()
inner_inner_class_obj=inner_class_obj.inner_inner()
