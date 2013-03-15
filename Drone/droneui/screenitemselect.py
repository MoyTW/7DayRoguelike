__author__ = 'Travis Moy'

import pyglet


def create_sprites_and_labels(labels, sprites, batch, current_page, inventory):
    del labels[:]
    del sprites[:]

    labels.append(pyglet.text.Label(
        'Page {0} of {1}'.format(current_page, inventory.num_pages - 1),
        font_size=14, x=648, y=20))

    inventory_list = inventory.get_keys_and_entities_on_page(current_page)
    row = 8
    col = 0
    for key, entity in inventory_list:
        x_pos = 20 + col * 344
        y_pos = 100 + row * 64
        row -= 1
        if row < 0:
            row = 8
            col += 1

        if entity is not None:
            text = "{0} - {1}".format(key, entity.name)
            sprites.append(pyglet.sprite.Sprite(entity.get_image(), x=x_pos, y=y_pos, batch=batch))
            sprites[-1].scale = .75
        else:
            text = "{0} - Empty".format(key)

        labels.append(pyglet.text.Label(text, font_size=14, x=x_pos + 56, y=y_pos + 19))