try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class ScreenObjects:

    def __init__(self, img_url, scale, base, start_at):
        self.img = simplegui.load_image(img_url)
        self.img_w = self.img.get_width()
        self.img_h = self.img.get_height()
        self.scaled_img_w = self.img_w / scale
        self.scaled_img_h = self.img_h / scale
        self.base = base
        self.animate_at_w = start_at

    def animate(self, canvas):
        canvas.draw_image(self.img,
                          (self.img_w / 2, self.img_h / 2),

                          (self.img_w, self.img_h),
                          (self.animate_at_w / 2, self.base),
                          (self.scaled_img_w, self.scaled_img_h))

    def update(self, offset):
        self.animate_at_w -= offset

    def set_animate_at_w(self, animate_at_w):
        self.animate_at_w = animate_at_w


class Obstacle(ScreenObjects):

    def __init__(self, img_url, scale, base, start_at):
        super(Obstacle, self).__init__(img_url, scale, base, start_at)

    def get_scaled_img_w(self):
        return self.scaled_img_w