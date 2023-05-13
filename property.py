class Property:
    def __init__(self, square_feet='', bedrooms='', bathrooms='', *args, **kwargs):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.square_feet = square_feet

    def display(self):
        print(f'Property Details\n'
              f'================\n'
              f'Square Feet: {self.square_feet}\n'
              f'Bedrooms: {self.bedrooms}\n'
              f'Bathrooms: {self.bathrooms}')

    def prompt_init():
        return dict(
            square_feet=input("Square Feet: "),
            bedrooms=input("Bedrooms: "),
            bathrooms=input("Bathrooms: ")
        )

    prompt_init = staticmethod(prompt_init)
# Instance method vs static method
# Instance methodları sadece ilgili sınıftan instance aldığımızda. instance ismi üzerinden çağırarak kullanabiliriz. Bugüne kadar hep bu yöntemi kullandık. Burada 'display' isimli method gene bu yapıya örnektir.
# Static methodlar ise ilgili sınıfın örneklemi alınmadan direk sınıf ismi üzerinden çağırarak kullandığımız methodlardır. Python içerisinde built-in olarak bulunan 'math' sınıfı içerisindeki methdolar buna örnektir. Burada ise 'promp_init' methodunu static işaretledik. Böylelikle 'Property' sınıfından örneklem almadan bu methodu kullanabileceğim.
# Static methodlar kulağa çok hoş gelmektedir. Lakin uygulamadı her methodumuzu statik işaretlemeyiz. Bunun nedeni ise static methodların RAM'in Heap alanında ki yaşama şekilidir. Static olarak işaretlenmiş herşey RAM Heap alanında projenin koştuğu server reset edilinceye kadar yaşar. Intance methodlar ise görevlerini icra ettikten sonra Garbage Collector tarafından RAM'in Heap alanından silinirler.

