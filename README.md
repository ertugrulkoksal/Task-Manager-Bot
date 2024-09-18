# Discord Görev Yönetim Botu

Bu bot, Discord'da küçük ekiplerde görev yönetimi yapmanıza yardımcı olur. Görev ekleme, silme, görüntüleme ve tamamlama özelliklerine sahiptir.

## Kurulum

### Adım Adım:
1. Botun çalışması için gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. Discord Developer Portal'da bir bot oluşturun.
    - Botu oluştururken, **mesaj okuma iznini (Message Content Intent)** etkinleştirdiğinizden emin olun.
    - Botun diğer gerekli izinlerini de kontrol etmeyi unutmayın.

3. Botu sunucunuza ekleyin.

4. `bot.py` dosyasındaki şu satıra Discord token'ınızı girin:
    ```python
    bot.run('YOUR_DISCORD_TOKEN')
    ```

### Terminalden Çalıştırma
1. Aşağıdaki komutları terminalde çalıştırın:
    ```bash
    pip install -r requirements.txt
    python bot.py
    ```

2. Discord sunucunuza gidin ve botun çalıştığından emin olun. Hepsi bu kadar!

## Komutlar

İşte botla kullanabileceğiniz komutlar:

- **`!add_task <açıklama>`** — Yeni bir görev ekler.
- **`!delete_task <task_id>`** — Belirtilen ID'ye sahip görevi siler.
- **`!show_tasks`** — Tüm görevleri listeler.
- **`!complete_task <task_id>`** — Görevi tamamlanmış olarak işaretler.

## Örnek Kullanım:

- Yeni bir görev eklemek için:
    ```
    !add_task Örnek görev
    ```

- Tüm görevleri görmek için:
    ```
    !show_tasks
    ```

- Bir görevi tamamlamak için:
    ```
    !complete_task 1
    ```

- Bir görevi silmek için:
    ```
    !delete_task 1
    ```

İşte bu kadar basit! Discord sunucunda görev yönetimini kolaylaştırmak için botunu kullanmaya başlayabilirsin.

### Not:
Eğer bot komutlara cevap vermiyorsa, botun yetkilerini ve izinlerini kontrol et. Ayrıca **Message Content Intent** ayarını etkinleştirdiğinden emin ol.
