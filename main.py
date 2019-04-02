"""
Still have to write the docstring.
"""

############################################# Imports ##############################################

import math
from random import randint
from random import uniform

import pygame

######################################### Global variables #########################################

__author__ = 'P. Cassiman'
__version__ = '0.2.0'

############################################# Classes ##############################################


class Vector(object):
    """
    Class to represent points. This class is then used to represent higher shapes, such as lines,
    planes, polygons etc.
    The vector class is based on this class.
    """

    def __init__(self, x: [int, float] = 0, y: [int, float] = 0):
        """
        Constructor for the Vector class. The coordinates are given in a cartesian way.

        Keyword Arguments:
            x {int, float} -- The x coordinate of the point. (default: {0})
            y {int, float} -- The y coordinate of the point. (default: {0})
        """

        # Save the coordinates.
        self.x_coord = x
        self.y_coord = y

        return

    def __str__(self):
        """
        Method called when the str() method is used on the object.
        """

        # Return a string representation of the vector.
        return "Vector at ({}, {})".format(self.x_coord, self.y_coord)

    def __eq__(self, other):
        """
       Method called when the '==' operator is used on the object.
        """

        if isinstance(other, Vector):
            # If the other object is also a vector, we can compare them.
            if self.x_coord == other.x_coord and self.y_coord == other.y_coord:
                # If both vectors have the same x and y coordinates, they are equals.
                return True

            else:
                # If they do not have the same coordinates, they are not equals.
                return False

        else:
            # If the other object is not a vector raise TypeError.
            raise TypeError(
                "Expected Vector object for comparison, got{}".format(type(other)))

    def __lt__(self, other):
        """
        Method called when the '<' operator is used on the object.
        """

        if isinstance(other, Vector):
            magnitude1, _ = self.cartesian_to_polar(self.x_coord, self.y_coord)
            magnitude2, _ = other.cartesian_to_polar(
                other.x_coord, other.y_coord)

            if magnitude1 < magnitude2:
                return True

            else:
                return False

        else:
            # If the other object is not a vector raise TypeError.
            raise TypeError(
                "Expected Vector object for comparison, got{}".format(type(other)))

    def __le__(self, other):
        """
        Method called when the '<=' operator is used on the object.
        """

        if isinstance(other, Vector):
            magnitude1, _ = self.cartesian_to_polar(self.x_coord, self.y_coord)
            magnitude2, _ = other.cartesian_to_polar(
                other.x_coord, other.y_coord)

            if magnitude1 <= magnitude2:
                return True

            else:
                return False

        else:
            # If the other object is not a vector raise TypeError.
            raise TypeError(
                "Expected Vector object for comparison, got{}".format(type(other)))

    def __gt__(self, other):
        """
        Method called when the '>' operator is used on the object.
        """

        if isinstance(other, Vector):
            magnitude1, _ = self.cartesian_to_polar(self.x_coord, self.y_coord)
            magnitude2, _ = other.cartesian_to_polar(
                other.x_coord, other.y_coord)

            if magnitude1 > magnitude2:
                return True

            else:
                return False

        else:
            # If the other object is not a vector raise TypeError.
            raise TypeError(
                "Expected Vector object for comparison, got{}".format(type(other)))

    def __ge__(self, other):
        """
        Method called when the '>=' operator is used on the object.
        """

        if isinstance(other, Vector):
            magnitude1, _ = self.cartesian_to_polar(self.x_coord, self.y_coord)
            magnitude2, _ = other.cartesian_to_polar(
                other.x_coord, other.y_coord)

            if magnitude1 >= magnitude2:
                return True

            else:
                return False

        else:
            # If the other object is not a vector raise TypeError.
            raise TypeError(
                "Expected Vector object for comparison, got{}".format(type(other)))

    def __pos__(self):
        """
        Method called when the "+" operator is used on the point object. As a way of getting the
        positive value of the object.

        Returns:
            Vector -- A point object with the new coordinates.
        """

        # Return a new vector with the current coordinates.
        return Vector(self.x_coord, self.y_coord)

    def __neg__(self):
        """
        Method called when the "-" operator is used on the point object. As a way of getting the
        negative value of the object.

        Returns:
            Vector -- A point object with the new coordinates.
        """

        # Return a vector with inverted coordinates.
        return Vector(-self.x_coord, -self.y_coord)

    def __invert__(self):
        """
        Method called when the "~" operator is used on the point object. As a way of getting the
        negative value of the object (negating the object).

        This function relies on the __neg__ method, as they are the same in this context.

        Returns:
            Vector -- A point object with the new coordinates.
        """

        # Return an inverse of self (a vector).
        return -self

    def __add__(self, other):
        """
        Method called when the "+" operator is used on the point object.

        Returns:
            Vector -- A point object with the new coordinates.
        """

        if isinstance(other, Vector):
            # If the other object is another vector, add the coordinates.
            x_res = self.x_coord + other.x_coord
            y_res = self.y_coord + other.y_coord

        elif isinstance(other, (int, float)):
            # If the other object is a scalar, add the value to both coordinates.
            x_res = self.x_coord + other
            y_res = self.y_coord + other

        else:
            # If the other object has a different type than what we expected, raise an error.
            raise TypeError(
                "Expected Vector, int or float, got{}".format(type(other)))

        # Return a vector object with the new coordinates.
        return Vector(x_res, y_res)

    def __sub__(self, other):
        """
        Method called when the "-" operator is used on the vector object.

        Returns:
            Vector -- A vector object with the new coordinates.
        """

        if isinstance(other, Vector):
            # If the other object is another vector, subtract the coordinates.
            x_res = self.x_coord - other.x_coord
            y_res = self.y_coord - other.y_coord

        elif isinstance(other, (int, float)):
            # If the other object is a scalar, subtract the value from the coordinates.
            x_res = self.x_coord - other
            y_res = self.y_coord - other

        else:
            # If the other object has a different type than what we expected, raise an error.
            raise TypeError(
                "Expected Vector, int or float, got{}".format(type(other)))

        # Return a vector object with the new coordinates.
        return Vector(x_res, y_res)

    def __mul__(self, other):
        """
        Method called when the "*" operator is used on the vector object.

        Returns:
            Vector -- A vector object with the new coordinates.
        """

        if isinstance(other, (int, float)):
            # If the other object is a scalar, multiply the coordinates by the value.
            x_res = self.x_coord * other
            y_res = self.y_coord * other

        else:
            # If the other object has a different type than what we expected, raise an error.
            raise TypeError(
                "Expected int or float, got{}".format(type(other)))

        # Return a vector object with the new coordinates.
        return Vector(x_res, y_res)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other != 0:
                x_res = self.x_coord / other
                y_res = self.y_coord / other
            else:
                raise ValueError("Cannot divide by zero!")

            return Vector(x_res, y_res)
        else:
            raise TypeError("Vector can only be divided by a scalar.")

    def limit(self, value: [int, float] = 1):
        """
        Method to limit the magnitude of a vector to the given value.

        Arguments:
            value {int, float} -- The limit in magnitude for the vector.
        """

        magnitude, theta = self.cartesian_to_polar(self.x_coord, self.y_coord)

        magnitude = min(magnitude, value)

        x_temp, y_temp = self.polar_to_cartesian(magnitude, theta)

        self.x_coord = x_temp
        self.y_coord = y_temp

        return

    def distance_to(self, other):
        """
        Method to calculate the distance between two vectors.

        Arguments:
            other {Vector} -- The vector to calculate the distance to.

        Raises:
            TypeError -- If the other object is not a Vector.

        Returns:
            float -- The distance to the other Vector.
        """

        if isinstance(other, Vector):
            return math.sqrt(((self.x_coord - other.x_coord) ** 2) +
                             ((self.y_coord - other.y_coord) ** 2))

        else:
            # If the other object has a different type than what we expected, raise an error.
            raise TypeError("Expected Vector, got{}".format(type(other)))

    def invert(self):
        """
        Method to return the inverse of a vector.
        """

        return -self

    def rotate(self, angle: [int, float] = 0):
        """
        Method to rotate a vector around the Origin. The angle is given in degrees.

        Keyword Arguments:
            angle {int, float} -- Angle to rotate by. (default: {0})
        """

        # Convert the angle to radians.
        angle = math.radians(angle)

        # Temporarily save the current coordinates.
        x_temp = self.x_coord
        y_temp = self.y_coord

        # Calculate the new coordinates.
        self.x_coord = (x_temp * math.cos(angle)) - (y_temp * math.sin(angle))
        self.y_coord = (x_temp * math.sin(angle)) + (y_temp * math.cos(angle))

        return

    def translate(self, vector):
        """
        Method to translate a vector by a second vector.

        Arguments:
            vector {Vector} -- The translation vector.
        """

        self.x_coord += vector.x_coord
        self.y_coord += vector.y_coord

        return

    def get_magnitude(self):
        """
        method to return the magnitude of a vector.

        Returns:
            float -- The magnitude of a vector.
        """

        magnitude, _ = self.cartesian_to_polar(self.x_coord, self.y_coord)

        return magnitude

    def set_magnitude(self, magnitude):
        """
        Method to set the magnitude of a vector.
        """

        _, theta = self.cartesian_to_polar(self.x_coord, self.y_coord)

        x_temp, y_temp = self.polar_to_cartesian(magnitude, theta)

        self.x_coord = x_temp
        self.y_coord = y_temp

        return

    def get_direction(self):
        """
        Method to return the direction of a vector.

        Returns:
            float -- The direction of a vector in degrees.
        """

        _, direction = self.cartesian_to_polar(self.x_coord, self.y_coord)

        return math.degrees(direction)

    def get_tuple(self):
        """
        Method to return a tuple of the coordinates of the vector.

        Returns:
            tuple -- tuple representing the coordinates.
        """

        return (self.x_coord, self.y_coord)

    def normalize(self):
        """
        Method to return a normalized vector with magnitude one.
        """

        _, direction = self.cartesian_to_polar(self.x_coord, self.y_coord)

        x_val, y_val = self.polar_to_cartesian(1, direction)

        return Vector(x_val, y_val)

    @staticmethod
    def cartesian_to_polar(x_val: [int, float] = 0, y_val: [int, float] = 0):
        """
        Method to convert cartesian coordinates to polar coordinates.
        As opposed to the other methods in this class, this function returns arguments in radians.

        Keyword Arguments:
            x {int, float} -- x-coordinate (default: {0})
            y {int, float} -- y-coordinate (default: {0})

        Returns:
            float -- The magnitude of a vector.
            float -- The direction of a vector in radians.
        """

        if x_val != 0 and y_val != 0:
            # The magnitude is calculated using the pythagorean theorem.
            magnitude = math.sqrt((x_val ** 2) + (y_val ** 2))
            # The angle is calculated using the arc tangent.
            theta = math.atan(y_val / x_val)

            if x_val < 0:
                # If x is smaller than zero add 180 degrees to the angle (in radians).
                theta += math.pi

            if x_val > 0 and y_val < 0:
                # The fourth quadrant requires to add 360 degrees to the angle (to avoid negative
                # angle values).
                theta += math.tau

        elif x_val == 0 and y_val != 0:
            # If x is zero, the vector is pointing either up or down.
            # The magnitude is then depending on the y value.
            magnitude = abs(y_val)
            if y_val > 0:
                # If y is positive the angle is 90 degrees.
                theta = math.pi / 2
            else:
                # If y is positive the angle is 270 degrees.
                theta = math.pi * 3 / 2

        elif x_val != 0 and y_val == 0:
            # If y is zero, the vector is pointing either left or right.
            # The magnitude is then depending on the x value.
            magnitude = abs(x_val)
            if x_val > 0:
                # If x is positive the angle is 0 degrees.
                theta = 0
            else:
                # If x is positive the angle is 180 degrees.
                theta = math.pi
        else:
            # If we get some edge case, we return both the magnitude and angle as 0.
            magnitude = 0
            theta = 0

        # Modulo the angle for redundancy.
        theta = theta % math.tau
        # Return both parametres.
        return magnitude, theta

    @staticmethod
    def polar_to_cartesian(magnitude: [int, float], theta: [int, float]):
        """
        Method to convert polar coordinates to cartesian coordinates.
        As opposed to the other methods in this class, this function requires arguments in radians.

        Keyword Arguments:
            magnitude {int, float} -- magnitude (default: {0})
            theta {int, float} -- angle (default: {0})

        Returns:
            float -- The x-coordinate of a vector.
            float -- The y-coordinate of a vector.
        """

        # Calculate the x value.
        x_val = magnitude * math.cos(theta)
        # Calculate the y value.
        y_val = magnitude * math.sin(theta)

        return x_val, y_val



class Boid(object):
    """
    Class to represent boids for the flocking algorithm.
    """

    perception_radius = 50

    separation_factor = 0.25
    cohesion_factor = 2
    align_factor = 1

    def __init__(self):
        # self.position = Vector(WIDTH / 2, HEIGHT / 2)
        self.position = Vector(randint(0, WIDTH), randint(0, HEIGHT))
        self.velocity = Vector(uniform(-32, 32), uniform(-32, 32))
        self.acceleration = Vector()

        self.max_force = .5
        self.max_speed = 8

        self.update()

    def edges(self):
        """
        Method to allow the boids to wrap around the edges of the screen.
        """

        if self.position.x_coord > WIDTH:
            self.position.x_coord = 0
        elif self.position.x_coord < 0:
            self.position.x_coord = WIDTH

        if self.position.y_coord > HEIGHT:
            self.position.y_coord = 0
        elif self.position.y_coord < 0:
            self.position.y_coord = HEIGHT

        return

    def flock(self, boids):
        """
        Method to implement the three behaviors associated with the flocking algorithm.
        Alignment, cohesion and separation.

        Arguments:
            boids {list} -- The list of boids that compose the flock.
        """

        counter = 0

        align_vector = Vector()
        cohesion_vector = Vector()
        separation_vector = Vector()

        for other in boids:
            if other != self:
                distance = self.position.distance_to(other.position)
                if distance <= self.perception_radius:
                    counter += 1

                    align_vector += other.velocity

                    cohesion_vector += other.position

                    difference = self.position - other.position
                    if distance > 0:
                        difference /= distance
                        separation_vector += difference
                    counter += 1


            if counter > 0:
                align_vector /= counter
                # align_vector.set_magnitude(self.max_speed)
                align_vector -= self.velocity
                align_vector.limit(self.max_force)

                cohesion_vector /= counter
                cohesion_vector -= self.position
                # cohesion_vector.set_magnitude(self.max_speed)
                cohesion_vector -= self.velocity
                cohesion_vector.limit(self.max_force)

                separation_vector /= counter * 2
                # separation_vector.set_magnitude(self.max_speed)
                separation_vector -= self.velocity
                separation_vector.limit(self.max_force)


        self.acceleration -= (separation_vector * self.separation_factor)
        self.acceleration -= (align_vector * self.align_factor)
        self.acceleration -= (cohesion_vector * self.cohesion_factor)
        self.acceleration -= Vector(uniform(-.25, .25), uniform(-.25, .25))
        return

    def update(self):
        """
        Method to update the parametres of a boid.
        """
        self.velocity += self.acceleration
        self.velocity.limit(self.max_speed)
        self.position += self.velocity

        self.acceleration = Vector(0, 0)

        return

    def show(self, surface):
        """
        Method to draw the boids on the given surface. The target is a pygame window.

        Arguments:
            surface {pygame surface} -- The surface to draw the boid on.
        """

        pygame.draw.circle(surface,
                           (128, 255, 255),
                           (int(self.position.x_coord),
                            int(self.position.y_coord)),
                           3, 0)

        # Un-comment this block to see the perception radius around each boid.

        # pygame.draw.circle(surface,
        #                    (255, 0, 0),
        #                    (int(self.position.x_coord),
        #                     int(self.position.y_coord)),
        #                    self.perception_radius, 1)

############################################ Functions #############################################

############################################### Main ###############################################


if __name__ == "__main__":

    pygame.init()

    WIDTH = 800
    HEIGHT = 600

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Python flocking")

    RUN = True

    FLOCK = []
    for i in range(80):
        FLOCK.append(Boid())

    while RUN:
        pygame.time.delay(int(1000/60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        WIN.fill((0, 0, 32))

        OLD_FLOCK = FLOCK
        for boid in FLOCK:
            boid.flock(OLD_FLOCK)
            boid.update()
            boid.edges()
            boid.show(WIN)

        pygame.display.update()

    pygame.quit()
