class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            x1 <= self.pos_x <= x2 
            and y1 <= self.pos_y <= y2
        ) 


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range
        
        x1 = self.pos_x - width/2
        y1 = self.pos_y - height/2
        x2 = self.pos_x + width/2
        y2 = self.pos_y + height/2
        self.__hit_box = Rectangle(x1, y1, x2, y2)

    def in_area(self, x1, y1, x2, y2):
        rect = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(rect)


class Rectangle:
    def overlaps(self, rect):
        if (
                rect.get_left_x() <= self.get_right_x() 
                and rect.get_bottom_y() <= self.get_top_y()
        ):
            return True
        return False

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"


