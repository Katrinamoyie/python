class Smartphone:
    def __init__(self, color, camera, display):
        self.color = color
        self.camera = camera
        self.display = display

    def feat(self):
        return f"The phone has a {self.color} color, a {self.display} display, and a {self.camera} camera."
    
    # Derived class 1 (Android)
class Android(Smartphone):
    def feat(self):
        return f"Android: {self.get_color()} phone with {self._display} display and {self._camera} camera. Perfect for customization."

# Derived class 2 (iPhone)
class iPhone(Smartphone):
    def feat(self):
        return f"iPhone: {self.get_color()} phone with {self._display} display and {self._camera} camera. Known for seamless iOS integration."

# Polymorphic behavior in action
def phone_features(phone):
    print(phone.feat())

# Create instances of Android and iPhone
android_phone = Android("midnight black", "50MP", "6.7-inch")
iphone_phone = iPhone("silver", "48MP", "6.1-inch")

# Demonstrating encapsulation
android_phone.set_color("space gray")
print(f"Updated Android color: {android_phone.get_color()}")

# Demonstrate polymorphism
phone_features(android_phone)  # Android-specific feature method
phone_features(iphone_phone) 
        
phone1 = Smartphone("30mp","6.o d","rosegold")
phone2 = Smartphone("50mp", "4.0","midnightblack")
phone3= Smartphone("rosegold", "30MP", "6.0 inch")
phone4= Smartphone("midnight black", "50MP", "4.0 inch")


print(phone1.feat())
print(phone2.feat())