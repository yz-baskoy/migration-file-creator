import os
import datetime
import sys
import locale
import re

def get_messages():
    locale.setlocale(locale.LC_ALL, '')
    system_locale = locale.getlocale()[0]

    messages = {
        'en': {
            'usage': "Usage: python script.py <migration_name>",
            'file_exists': "Error: A file named {0} already exists.",
            'warning_newer_file': "\033[93mWarning:\033[0m The file {0} has a more recent date than the file being created.",
            'success': "Migration file \033[92msuccessfully\033[0m created: {0}",
            'namespace_not_found': "\033[93mWarning:\033[0m Unable to determine namespace from existing files. Using default '{0}'.",
        },
        'tr': {
            'usage': "Kullanım: python script.py <migration_name>",
            'file_exists': "Hata: {0} isimli bir dosya zaten mevcut.",
            'warning_newer_file': "\033[93mUyarı:\033[0m {0} dosyası, yeni oluşturulacak dosyadan daha yeni bir tarihte.",
            'success': "Migration dosyası \033[92mbaşarıyla\033[0m oluşturuldu: {0}",
            'namespace_not_found': "\033[93mUyarı:\033[0m Mevcut dosyalardan namespace belirlenemedi. Varsayılan '{0}' kullanılıyor.",
        }
    }

    return messages['tr'] if system_locale and system_locale.startswith('tr') else messages['en']

def determine_namespace(migrations_dir, default_namespace="YourNamespace.Migrations"):
    for filename in os.listdir(migrations_dir):
        if filename.endswith('.cs'):
            with open(os.path.join(migrations_dir, filename), 'r') as file:
                content = file.read()
                match = re.search(r'namespace\s+([\w.]+);', content)
                if match:
                    return match.group(1)
    return default_namespace

def create_migration(migration_name):
    msgs = get_messages()
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    
    filename = f"{timestamp}_{migration_name}.cs"
    migrations_dir = os.path.join(os.path.dirname(__file__), "Migrations")
    os.makedirs(migrations_dir, exist_ok=True)
    full_path = os.path.join(migrations_dir, filename)
    
    if os.path.exists(full_path):
        print(msgs['file_exists'].format(filename))
        return
    
    existing_files = os.listdir(migrations_dir)
    for existing_file in existing_files:
        if existing_file > filename:
            print(msgs['warning_newer_file'].format(existing_file))
    
    default_namespace = "YourNamespace.Migrations"
    namespace = determine_namespace(migrations_dir, default_namespace)
    if namespace == default_namespace:
        print(msgs['namespace_not_found'].format(default_namespace))

    content = f"""using FluentMigrator;

namespace {namespace};

[Migration({timestamp})]
public class _{timestamp}_{migration_name} : Migration
{{
    public override void Up()
    {{
    }}

    public override void Down()
    {{
    }}
}}
"""
    
    with open(full_path, "w") as f:
        f.write(content)
    
    print(msgs['success'].format(full_path))

if __name__ == "__main__":
    msgs = get_messages()
    if len(sys.argv) != 2:
        print(msgs['usage'])
    else:
        create_migration(sys.argv[1])