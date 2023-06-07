# Generated by Django 2.0.10 on 2019-04-24 10:27

import wagtail.blocks as wagtail_blocks
import wagtail.blocks.field_block as wagtail_field_block
import wagtail.fields as wagtail_fields
import wagtail.images.blocks
from django.db import migrations

import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_Hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail_fields.StreamField([('action_link', wagtail_blocks.StructBlock([('text', wagtail_blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail_blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail_blocks.BooleanBlock(label='Open in new window', required=False))])), ('care_card', wagtail_blocks.StructBlock([('type', wagtail_blocks.ChoiceBlock(choices=[('primary', 'Non-urgent'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('title', wagtail_blocks.CharBlock(required=True)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('details', wagtail_blocks.StructBlock([('title', wagtail_blocks.CharBlock(required=True)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('do_list', wagtail_blocks.StructBlock([('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('do', wagtail_blocks.ListBlock(wagtail_field_block.RichTextBlock))])), ('dont_list', wagtail_blocks.StructBlock([('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('dont', wagtail_blocks.ListBlock(wagtail_field_block.RichTextBlock))])), ('expander', wagtail_blocks.StructBlock([('title', wagtail_blocks.CharBlock(required=True)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('expander_group', wagtail_blocks.StructBlock([('expanders', wagtail_blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('inset_text', wagtail_blocks.StructBlock([('body', wagtail_blocks.RichTextBlock(required=True))])), ('image', wagtail_blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail_blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail_blocks.CharBlock(required=False))])), ('panel', wagtail_blocks.StructBlock([('label', wagtail_blocks.CharBlock(required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('panel_list', wagtail_blocks.StructBlock([('panels', wagtail_blocks.ListBlock(wagtail_blocks.StructBlock([('left_panel', wagtail_blocks.StructBlock([('label', wagtail_blocks.CharBlock(required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('right_panel', wagtail_blocks.StructBlock([('label', wagtail_blocks.CharBlock(required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail_blocks.RichTextBlock(required=True))]))])))])), ('grey_panel', wagtail_blocks.StructBlock([('label', wagtail_blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail_blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail_blocks.StructBlock([('title', wagtail_blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail_blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail_blocks.RichTextBlock(required=True))]))]),
        ),
    ]
