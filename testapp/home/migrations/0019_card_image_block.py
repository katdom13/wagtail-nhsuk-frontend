# Generated by Django 3.1.5 on 2021-01-19 17:27

from django.db import migrations
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    import wagtail.blocks as wagtail_blocks
    import wagtail.fields as wagtail_fields
else:
    import wagtail.core.blocks as wagtail_blocks
    import wagtail.core.fields as wagtail_fields
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_card_clickable_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspage',
            name='body',
            field=wagtail_fields.StreamField([('promo', wagtail_blocks.StructBlock([('url', wagtail_blocks.URLBlock(label='URL', required=True)), ('heading', wagtail_blocks.CharBlock(required=True)), ('description', wagtail_blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail_blocks.CharBlock(required=False)), ('size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.', max_value=6, min_value=2))])), ('promo_group', wagtail_blocks.StructBlock([('column', wagtail_blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('promos', wagtail_blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))])), ('card_basic', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False))])), ('card_clickable', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False)), ('internal_page', wagtail_blocks.PageChooserBlock(help_text='Interal Page Link for the card', label='Internal Page', required=False)), ('url', wagtail_blocks.URLBlock(help_text='External Link for the card', label='URL', required=False))])), ('card_image', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('alt_text', wagtail_blocks.CharBlock(required=True)), ('url', wagtail_blocks.URLBlock(help_text='Optional, if there is a link the entire card will be clickable.', label='URL', required=False)), ('internal_page', wagtail_blocks.PageChooserBlock(help_text='Optional, if there is a link the entire card will be clickable.', label='Internal Page', required=False))])), ('card_feature', wagtail_blocks.StructBlock([('feature_heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('card_group', wagtail_blocks.StructBlock([('column', wagtail_blocks.ChoiceBlock(choices=[('', 'Full-width'), ('one-half', 'One-half'), ('one-third', 'One-third')], required=False)), ('body', wagtail_blocks.StreamBlock([('card_basic', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False))])), ('card_clickable', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False)), ('internal_page', wagtail_blocks.PageChooserBlock(help_text='Interal Page Link for the card', label='Internal Page', required=False)), ('url', wagtail_blocks.URLBlock(help_text='External Link for the card', label='URL', required=False))])), ('card_image', wagtail_blocks.StructBlock([('heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('alt_text', wagtail_blocks.CharBlock(required=True)), ('url', wagtail_blocks.URLBlock(help_text='Optional, if there is a link the entire card will be clickable.', label='URL', required=False)), ('internal_page', wagtail_blocks.PageChooserBlock(help_text='Optional, if there is a link the entire card will be clickable.', label='Internal Page', required=False))])), ('card_feature', wagtail_blocks.StructBlock([('feature_heading', wagtail_blocks.CharBlock(required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=6.', max_value=6, min_value=2)), ('heading_size', wagtail_blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text="The heading size affects the visual size, this follows the front-end library's sizing.", required=False)), ('body', wagtail_blocks.RichTextBlock(required=True))]))], required=True))]))]),
        ),
    ]
