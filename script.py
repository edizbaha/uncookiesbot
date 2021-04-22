class Script(object):

    START_MSG = """<b>Merhaba {},

Ben @busununkiyafetleri tarafından yapılmış filtre yönetim botuyum.

Yardım için <i>/help</i> komutunu yazınız.</b>
"""


    HELP_MSG = """
<i>Botu kullanabilmek için gruba yönetici olarak ekleyin</i>

<b>Genel Komutlar:</b>
/start - Çalıştığımı kontrol et
/help - Yardım komutu
/about - Hakkımda

<b>Filtre Komutları:</b>
/add <code>filtre ismi yanıt</code> - Yeni filtre
/del <code>filtre ismi</code> - Filtreyi sil
/delall - Tüm filtreleri sil (Sadece yönetici)
/viewfilters - Tüm filtreleri listeler

<b>Bağlantı Komutları:</b>
/connect <code><grup id></code> - Grubu sohbete bağla
/connections - Bağlantıları yönet


<b>Ekstra Özellikler:</b>
/status - Botun durumu (Sadece yönetici)
/id - ID bilgisini öğrenme
/info <code><kullanıcı idsi></code> Kişi hakkında detaylı bilgi
"""


    ABOUT_MSG = """<b>Uncookies Bot</b>

<b>Kodlayan: </b> @busununkiyafetleri  
<b>Program Dili:</b> <code>Python3</code>
<b>Kütüphane:</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""