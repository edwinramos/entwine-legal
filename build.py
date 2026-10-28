# Generates the static legal pages for Entwine (es/en/fr). Run: python3 build.py
import os, html
EMAIL = "edwinramos.93@gmail.com"
DATE = {"es": "27 de octubre de 2026", "en": "October 27, 2026", "fr": "27 octobre 2026"}
LANGS = {"es": "Español", "en": "English", "fr": "Français"}

T = {
"es": {
 "nav": ["Privacidad", "Términos", "Eliminar datos"],
 "updated": "Última actualización",
 "home_title": "Entwine · Información legal",
 "home_intro": "Entwine es una app para parejas adultas (18+) que comparten retos íntimos y discretos entre dos teléfonos.",
 "privacy_title": "Política de privacidad",
 "privacy": [
  ("Quién es responsable", f"Entwine es desarrollada por Edwin Ramos Madera, desarrollador independiente (el «desarrollador»). Contacto: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
  ("Resumen", "Entwine no muestra publicidad, no usa SDK de analítica ni de rastreo, no vende datos y no crea cuentas con email ni contraseña. La app funciona con un identificador anónimo y con una «sala» compartida entre exactamente dos dispositivos."),
  ("Datos que tratamos", "<ul><li><b>Apodo</b> que escribes al empezar (por ejemplo «Amor»). Se guarda en tu dispositivo y en la sala compartida para que tu pareja lo vea.</li><li><b>Contenido de la pareja</b>: el reto activo y su progreso, los retos propios que creéis, los recuerdos de la Bóveda (texto), el tono elegido y ajustes compartidos (modo discreto, pausa).</li><li><b>Identificador anónimo</b> de Firebase Authentication (un uid aleatorio, sin nombre ni email) y el código de vinculación de 6 caracteres de la sala.</li><li><b>Token de notificaciones push</b> de Expo de cada dispositivo, para avisar a tu pareja.</li><li><b>Estado de la suscripción e historial de compras</b> del plan Dúo, gestionados por Google Play Billing. Si quien paga tiene el plan activo, la sala guarda una marca de suscripción (activa o no, producto, plan y fecha hasta la que vale) que tu pareja puede ver; no se guardan tokens de compra ni datos de pago. El desarrollador nunca recibe los datos de tu tarjeta.</li><li><b>Identificador de cuenta para Google Play</b>: al comprar, se envía a Google Play tu uid anónimo como identificador ofuscado de la compra.</li><li><b>Datos técnicos</b> que los proveedores registran al prestar el servicio (por ejemplo, dirección IP y tipo de dispositivo).</li></ul>"),
  ("Datos que NO tratamos", "No accedemos a tu ubicación, contactos, fotos, micrófono ni cámara. El desbloqueo de la Bóveda con huella, rostro o PIN lo hace el sistema operativo; la app nunca recibe datos biométricos."),
  ("Para qué los usamos", "Únicamente para que la app funcione: sincronizar en tiempo real la sala entre los dos dispositivos, enviar recordatorios y avisos a tu pareja, y activar el plan Dúo para los dos miembros de la sala."),
  ("Dónde se guardan y quién puede verlos", "Los datos de la sala se guardan en Firebase Realtime Database (Google). Las reglas de seguridad solo permiten leer y escribir la sala a los dos identificadores anónimos que la forman. Los datos viajan cifrados (HTTPS) y Google los cifra en reposo en sus servidores, pero <b>no usan cifrado de extremo a extremo</b>: técnicamente son accesibles para el proveedor de infraestructura. Una copia se guarda también en el almacenamiento local de tu dispositivo."),
  ("Proveedores (encargados del tratamiento)", "<ul><li><b>Google Firebase</b> (Authentication anónima y Realtime Database) — <a href=\"https://firebase.google.com/support/privacy\">privacidad</a>.</li><li><b>Expo (650 Industries)</b> — servicio de notificaciones push, que entrega los avisos a través de Firebase Cloud Messaging de Google — <a href=\"https://expo.dev/privacy\">privacidad</a>.</li><li><b>Google Play (Google Play Billing)</b> — pagos, facturación y estado de la suscripción — <a href=\"https://policies.google.com/privacy\">privacidad</a>.</li></ul>No compartimos datos con nadie más ni los usamos para publicidad."),
  ("Conservación", "Los datos de la sala se conservan mientras la pareja la use. Se eliminan de inmediato cuando cualquiera de los dos miembros usa «Salir de la pareja y borrar datos» (en Ajustes), lo que borra la sala para ambos. Si lo solicitas por email, los eliminaremos en un máximo de 30 días. Google Play conserva los registros de compra el tiempo que exijan sus obligaciones legales y contables."),
  ("Tus derechos", "Puedes acceder, corregir o eliminar tus datos en cualquier momento desde la app o escribiendo a <a href=\"mailto:{0}\">{0}</a>. Consulta <a href=\"delete-data.html\">cómo eliminar tus datos</a>.".format(EMAIL)),
  ("Solo para adultos", "Entwine está dirigida exclusivamente a personas mayores de 18 años. No recopilamos a sabiendas datos de menores; si crees que un menor está usando la app, escríbenos y eliminaremos sus datos."),
  ("Cambios", "Si cambiamos esta política, publicaremos la nueva versión en esta página con su fecha de actualización."),
 ],
 "terms_title": "Términos de uso",
 "terms": [
  ("Aceptación", "Al usar Entwine aceptas estos términos. Si no estás de acuerdo, no uses la app."),
  ("Edad mínima", "Debes tener al menos 18 años. Entwine contiene temas románticos y sensuales para parejas adultas que participan de forma voluntaria."),
  ("Consentimiento y uso responsable", "Los retos son sugerencias. Cada persona decide libremente si participa y puede detenerse en cualquier momento. Respeta siempre los límites y el consentimiento de tu pareja. No uses la app para presionar, acosar ni dañar a nadie."),
  ("Tu contenido", "Eres responsable del contenido que escribes (apodo, retos propios, recuerdos de la Bóveda). No publiques contenido ilegal ni datos de terceros sin su permiso. Ese contenido solo se comparte con el otro miembro de tu sala."),
  ("Plan Dúo (suscripción)", "Algunas funciones requieren el plan Dúo. Se contrata y se cobra a través de Google Play, se renueva automáticamente al final de cada periodo y puedes cancelarlo en cualquier momento en Google Play &gt; Pagos y suscripciones. Una suscripción activa cubre a los dos miembros de la sala mientras ambos permanezcan vinculados. Los reembolsos se rigen por las políticas de Google Play. Puedes restaurar tus compras desde la propia app."),
  ("Disponibilidad", "La app se ofrece «tal cual». Intentamos que funcione bien, pero no garantizamos que esté libre de errores ni disponible sin interrupciones, y el contenido puede cambiar."),
  ("Responsabilidad", "En la medida permitida por la ley, el desarrollador no será responsable de daños indirectos derivados del uso de la app. Nada en estos términos limita los derechos que te reconozca la ley aplicable."),
  ("Terminación", "Puedes dejar de usar la app y borrar tus datos cuando quieras. Podemos suspender el acceso si se usa la app de forma abusiva o ilegal."),
  ("Ley aplicable", "Estos términos se rigen por las leyes de la República Dominicana, sin perjuicio de las normas imperativas de protección al consumidor de tu país."),
  ("Contacto", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
 ],
 "delete_title": "Eliminar tus datos",
 "delete": [
  ("Desde la app (inmediato)", "<ol><li>Abre Entwine y ve a <b>Ajustes</b>.</li><li>Pulsa <b>«Salir de la pareja y borrar datos»</b> y confirma.</li></ol>Se borran al instante: la sala compartida (apodos, reto y progreso, retos propios, recuerdos de la Bóveda, tokens de notificaciones), el código de vinculación, tu identificador anónimo y todos los datos guardados en el dispositivo. La sala se elimina <b>para los dos miembros</b> de la pareja."),
  ("Sin acceso a la app", "Si ya desinstalaste la app o perdiste el teléfono, escribe a <a href=\"mailto:{0}?subject=Entwine%20-%20Eliminar%20datos\">{0}</a> con el asunto «Entwine - Eliminar datos» e indica el código de vinculación de tu sala (por ejemplo V9K-42M) si lo recuerdas. Eliminaremos los datos de esa sala en un máximo de 30 días. Desinstalar la app por sí solo no borra los datos de la sala en la nube.".format(EMAIL)),
  ("Qué se conserva", "Los registros de compra del plan Dúo los conserva Google Play según sus obligaciones legales. La marca de suscripción de la sala se borra junto con la sala. Para cancelar la suscripción ve a Google Play &gt; Pagos y suscripciones; borrar tus datos no cancela la suscripción automáticamente."),
 ],
},
"en": {
 "nav": ["Privacy", "Terms", "Delete data"],
 "updated": "Last updated",
 "home_title": "Entwine · Legal information",
 "home_intro": "Entwine is an app for adult couples (18+) who share intimate, discreet challenges across two phones.",
 "privacy_title": "Privacy policy",
 "privacy": [
  ("Who is responsible", f"Entwine is developed by Edwin Ramos Madera, an independent developer (the “developer”). Contact: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
  ("Summary", "Entwine shows no ads, uses no analytics or tracking SDKs, does not sell data and does not create email/password accounts. The app works with an anonymous identifier and a shared “room” between exactly two devices."),
  ("Data we process", "<ul><li><b>Nickname</b> you type when you start (e.g. “Love”). Stored on your device and in the shared room so your partner can see it.</li><li><b>Couple content</b>: the active challenge and its progress, custom challenges you create, Vault memories (text), the chosen tone and shared settings (discreet mode, pause).</li><li><b>Anonymous identifier</b> from Firebase Authentication (a random uid, no name or email) and the room’s 6-character pairing code.</li><li><b>Expo push notification token</b> of each device, used to notify your partner.</li><li><b>Subscription status and purchase history</b> for the Duo plan, handled by Google Play Billing. When the paying member has an active plan, the room stores a subscription flag (active or not, product, plan and the date it is valid until) that your partner can see; no purchase tokens or payment data are stored. The developer never receives your card details.</li><li><b>Account identifier for Google Play</b>: when you buy, your anonymous uid is sent to Google Play as the purchase’s obfuscated account identifier.</li><li><b>Technical data</b> logged by providers while delivering the service (e.g. IP address and device type).</li></ul>"),
  ("Data we do NOT process", "We do not access your location, contacts, photos, microphone or camera. Unlocking the Vault with fingerprint, face or PIN is handled by the operating system; the app never receives biometric data."),
  ("Why we use it", "Only to make the app work: sync the room in real time between the two devices, send reminders and partner notifications, and activate the Duo plan for both members of the room."),
  ("Where it is stored and who can see it", "Room data is stored in Firebase Realtime Database (Google). Security rules only allow the two anonymous identifiers that form the room to read and write it. Data is encrypted in transit (HTTPS) and Google encrypts it at rest on its servers, but it is <b>not end-to-end encrypted</b>: it is technically accessible to the infrastructure provider. A copy is also kept in your device’s local storage."),
  ("Providers (processors)", "<ul><li><b>Google Firebase</b> (anonymous Authentication and Realtime Database) — <a href=\"https://firebase.google.com/support/privacy\">privacy</a>.</li><li><b>Expo (650 Industries)</b> — push notification service, delivered through Google Firebase Cloud Messaging — <a href=\"https://expo.dev/privacy\">privacy</a>.</li><li><b>Google Play (Google Play Billing)</b> — subscription payments, billing and status — <a href=\"https://policies.google.com/privacy\">privacy</a>.</li></ul>We do not share data with anyone else or use it for advertising."),
  ("Retention", "Room data is kept while the couple uses it. It is deleted immediately when either member uses “Leave couple and delete data” (in Settings), which deletes the room for both. If you request it by email, we will delete it within 30 days. Google Play keeps purchase records as long as their legal and accounting obligations require."),
  ("Your rights", "You can access, correct or delete your data at any time from the app or by writing to <a href=\"mailto:{0}\">{0}</a>. See <a href=\"delete-data.html\">how to delete your data</a>.".format(EMAIL)),
  ("Adults only", "Entwine is intended exclusively for people aged 18 or over. We do not knowingly collect data from minors; if you believe a minor is using the app, contact us and we will delete their data."),
  ("Changes", "If we change this policy, we will publish the new version on this page with its update date."),
 ],
 "terms_title": "Terms of use",
 "terms": [
  ("Acceptance", "By using Entwine you accept these terms. If you do not agree, do not use the app."),
  ("Minimum age", "You must be at least 18 years old. Entwine contains romantic and sensual themes for consenting adult couples."),
  ("Consent and responsible use", "Challenges are suggestions. Each person freely decides whether to take part and can stop at any time. Always respect your partner’s limits and consent. Do not use the app to pressure, harass or harm anyone."),
  ("Your content", "You are responsible for the content you write (nickname, custom challenges, Vault memories). Do not post illegal content or third-party data without permission. This content is only shared with the other member of your room."),
  ("Duo plan (subscription)", "Some features require the Duo plan. It is purchased and billed through Google Play, renews automatically at the end of each period and can be cancelled at any time in Google Play &gt; Payments &amp; subscriptions. An active subscription covers both members of the room while they remain paired. Refunds follow Google Play policies. You can restore purchases from within the app."),
  ("Availability", "The app is provided “as is”. We try to keep it working well, but we do not guarantee it is error-free or uninterrupted, and content may change."),
  ("Liability", "To the extent permitted by law, the developer is not liable for indirect damages arising from use of the app. Nothing in these terms limits rights granted to you by applicable law."),
  ("Termination", "You can stop using the app and delete your data whenever you want. We may suspend access in case of abusive or illegal use."),
  ("Governing law", "These terms are governed by the laws of the Dominican Republic, without prejudice to mandatory consumer protection rules of your country."),
  ("Contact", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
 ],
 "delete_title": "Delete your data",
 "delete": [
  ("From the app (immediate)", "<ol><li>Open Entwine and go to <b>Settings</b>.</li><li>Tap <b>“Leave couple and delete data”</b> and confirm.</li></ol>This instantly deletes: the shared room (nicknames, challenge and progress, custom challenges, Vault memories, notification tokens), the pairing code, your anonymous identifier and all data stored on the device. The room is deleted <b>for both members</b> of the couple."),
  ("Without access to the app", "If you already uninstalled the app or lost your phone, email <a href=\"mailto:{0}?subject=Entwine%20-%20Delete%20data\">{0}</a> with the subject “Entwine - Delete data” and include your room’s pairing code (e.g. V9K-42M) if you remember it. We will delete that room’s data within 30 days. Uninstalling the app alone does not delete the room data in the cloud.".format(EMAIL)),
  ("What is kept", "Duo plan purchase records are kept by Google Play according to its legal obligations. The room’s subscription flag is deleted together with the room. To cancel the subscription go to Google Play &gt; Payments &amp; subscriptions; deleting your data does not cancel the subscription automatically."),
 ],
},
"fr": {
 "nav": ["Confidentialité", "Conditions", "Supprimer les données"],
 "updated": "Dernière mise à jour",
 "home_title": "Entwine · Informations légales",
 "home_intro": "Entwine est une application pour couples adultes (18+) qui partagent des défis intimes et discrets entre deux téléphones.",
 "privacy_title": "Politique de confidentialité",
 "privacy": [
  ("Responsable", f"Entwine est développée par Edwin Ramos Madera, développeur indépendant (le « développeur »). Contact : <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
  ("Résumé", "Entwine n’affiche pas de publicité, n’utilise aucun SDK d’analyse ou de suivi, ne vend pas de données et ne crée pas de comptes avec e-mail ou mot de passe. L’application fonctionne avec un identifiant anonyme et une « salle » partagée entre exactement deux appareils."),
  ("Données traitées", "<ul><li><b>Surnom</b> saisi au démarrage (par exemple « Mon cœur »). Stocké sur votre appareil et dans la salle partagée pour que votre partenaire le voie.</li><li><b>Contenu du couple</b> : le défi actif et sa progression, les défis personnalisés, les souvenirs du Coffre (texte), le ton choisi et les réglages partagés (mode discret, pause).</li><li><b>Identifiant anonyme</b> de Firebase Authentication (un uid aléatoire, sans nom ni e-mail) et le code d’appairage à 6 caractères de la salle.</li><li><b>Jeton de notifications push</b> Expo de chaque appareil, pour prévenir votre partenaire.</li><li><b>Statut d’abonnement et historique d’achats</b> du forfait Duo, gérés par Google Play Billing. Lorsque le membre qui paie a un forfait actif, la salle enregistre un indicateur d’abonnement (actif ou non, produit, formule et date de validité) visible par votre partenaire ; aucun jeton d’achat ni donnée de paiement n’est enregistré. Le développeur ne reçoit jamais vos données de carte.</li><li><b>Identifiant de compte pour Google Play</b> : lors d’un achat, votre uid anonyme est transmis à Google Play comme identifiant de compte obscurci de l’achat.</li><li><b>Données techniques</b> enregistrées par les prestataires pour fournir le service (par exemple adresse IP et type d’appareil).</li></ul>"),
  ("Données NON traitées", "Nous n’accédons pas à votre localisation, vos contacts, photos, micro ou caméra. Le déverrouillage du Coffre par empreinte, visage ou code est géré par le système ; l’application ne reçoit jamais de données biométriques."),
  ("Finalités", "Uniquement le fonctionnement de l’application : synchroniser la salle en temps réel entre les deux appareils, envoyer des rappels et des notifications au partenaire, et activer le forfait Duo pour les deux membres de la salle."),
  ("Stockage et accès", "Les données de la salle sont stockées dans Firebase Realtime Database (Google). Les règles de sécurité n’autorisent la lecture et l’écriture qu’aux deux identifiants anonymes qui forment la salle. Les données sont chiffrées en transit (HTTPS) et Google les chiffre au repos sur ses serveurs, mais elles <b>ne sont pas chiffrées de bout en bout</b> : elles restent techniquement accessibles au fournisseur d’infrastructure. Une copie est aussi conservée dans le stockage local de votre appareil."),
  ("Prestataires (sous-traitants)", "<ul><li><b>Google Firebase</b> (Authentication anonyme et Realtime Database) — <a href=\"https://firebase.google.com/support/privacy\">confidentialité</a>.</li><li><b>Expo (650 Industries)</b> — service de notifications push, acheminées via Firebase Cloud Messaging de Google — <a href=\"https://expo.dev/privacy\">confidentialité</a>.</li><li><b>Google Play (Google Play Billing)</b> — paiements, facturation et statut de l’abonnement — <a href=\"https://policies.google.com/privacy\">confidentialité</a>.</li></ul>Nous ne partageons pas les données avec d’autres tiers et ne les utilisons pas à des fins publicitaires."),
  ("Conservation", "Les données de la salle sont conservées tant que le couple l’utilise. Elles sont supprimées immédiatement lorsque l’un des deux membres utilise « Quitter le couple et supprimer les données » (dans Réglages), ce qui supprime la salle pour les deux. Sur demande par e-mail, nous les supprimerons sous 30 jours maximum. Google Play conserve les enregistrements d’achat selon leurs obligations légales et comptables."),
  ("Vos droits", "Vous pouvez accéder à vos données, les corriger ou les supprimer à tout moment depuis l’application ou en écrivant à <a href=\"mailto:{0}\">{0}</a>. Voir <a href=\"delete-data.html\">comment supprimer vos données</a>.".format(EMAIL)),
  ("Réservé aux adultes", "Entwine est destinée exclusivement aux personnes de 18 ans ou plus. Nous ne collectons pas sciemment de données de mineurs ; si vous pensez qu’un mineur utilise l’application, contactez-nous et nous supprimerons ses données."),
  ("Modifications", "En cas de modification de cette politique, la nouvelle version sera publiée sur cette page avec sa date de mise à jour."),
 ],
 "terms_title": "Conditions d’utilisation",
 "terms": [
  ("Acceptation", "En utilisant Entwine, vous acceptez ces conditions. Si vous n’êtes pas d’accord, n’utilisez pas l’application."),
  ("Âge minimum", "Vous devez avoir au moins 18 ans. Entwine contient des thèmes romantiques et sensuels destinés à des couples adultes consentants."),
  ("Consentement et usage responsable", "Les défis sont des suggestions. Chacun décide librement d’y participer et peut arrêter à tout moment. Respectez toujours les limites et le consentement de votre partenaire. N’utilisez pas l’application pour faire pression, harceler ou nuire à quiconque."),
  ("Votre contenu", "Vous êtes responsable du contenu que vous écrivez (surnom, défis personnalisés, souvenirs du Coffre). Ne publiez pas de contenu illégal ni de données de tiers sans leur accord. Ce contenu n’est partagé qu’avec l’autre membre de votre salle."),
  ("Forfait Duo (abonnement)", "Certaines fonctions nécessitent le forfait Duo. Il est souscrit et facturé via Google Play, se renouvelle automatiquement à la fin de chaque période et peut être résilié à tout moment dans Google Play &gt; Paiements et abonnements. Un abonnement actif couvre les deux membres de la salle tant qu’ils restent appairés. Les remboursements suivent les règles de Google Play. Vous pouvez restaurer vos achats depuis l’application."),
  ("Disponibilité", "L’application est fournie « en l’état ». Nous faisons de notre mieux, sans garantir l’absence d’erreurs ou d’interruptions ; le contenu peut évoluer."),
  ("Responsabilité", "Dans les limites autorisées par la loi, le développeur n’est pas responsable des dommages indirects liés à l’utilisation de l’application. Rien dans ces conditions ne limite les droits que vous accorde la loi applicable."),
  ("Résiliation", "Vous pouvez cesser d’utiliser l’application et supprimer vos données quand vous le souhaitez. Nous pouvons suspendre l’accès en cas d’usage abusif ou illégal."),
  ("Droit applicable", "Ces conditions sont régies par le droit de la République dominicaine, sans préjudice des règles impératives de protection des consommateurs de votre pays."),
  ("Contact", f"<a href=\"mailto:{EMAIL}\">{EMAIL}</a>"),
 ],
 "delete_title": "Supprimer vos données",
 "delete": [
  ("Depuis l’application (immédiat)", "<ol><li>Ouvrez Entwine et allez dans <b>Réglages</b>.</li><li>Touchez <b>« Quitter le couple et supprimer les données »</b> et confirmez.</li></ol>Sont supprimés immédiatement : la salle partagée (surnoms, défi et progression, défis personnalisés, souvenirs du Coffre, jetons de notifications), le code d’appairage, votre identifiant anonyme et toutes les données stockées sur l’appareil. La salle est supprimée <b>pour les deux membres</b> du couple."),
  ("Sans accès à l’application", "Si vous avez désinstallé l’application ou perdu votre téléphone, écrivez à <a href=\"mailto:{0}?subject=Entwine%20-%20Supprimer%20mes%20donn%C3%A9es\">{0}</a> avec l’objet « Entwine - Supprimer mes données » en indiquant le code d’appairage de votre salle (par exemple V9K-42M) si vous vous en souvenez. Nous supprimerons les données de cette salle sous 30 jours maximum. Désinstaller l’application ne supprime pas à lui seul les données de la salle dans le cloud.".format(EMAIL)),
  ("Ce qui est conservé", "Les enregistrements d’achat du forfait Duo sont conservés par Google Play selon ses obligations légales. L’indicateur d’abonnement de la salle est supprimé avec la salle. Pour résilier l’abonnement, allez dans Google Play &gt; Paiements et abonnements ; supprimer vos données ne résilie pas automatiquement l’abonnement."),
 ],
},
}

CSS = """:root{color-scheme:dark}body{margin:0;background:#131316;color:#e4e1e6;font:16px/1.65 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 22px 64px}a{color:#ffb2bc}h1{font-family:Georgia,serif;font-weight:400;font-size:2rem;margin:.2em 0 .1em}
h2{font-size:1.05rem;color:#E5A96A;letter-spacing:.02em;margin-top:2em}header{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between;border-bottom:1px solid #3a2e31;padding-bottom:14px}
.brand{font-family:Georgia,serif;font-size:1.3rem;color:#ffb2bc;text-decoration:none}nav a{margin-right:14px;font-size:.92rem}.langs a{margin-left:10px;font-size:.85rem;color:#a68a8d}
.updated{color:#a68a8d;font-size:.9rem}li{margin:.35em 0}footer{margin-top:48px;color:#6c6362;font-size:.85rem}"""

def page(lang, slug, title, sections):
    t = T[lang]
    nav = " ".join(f'<a href="{s}.html">{n}</a>' for s, n in zip(["privacy", "terms", "delete-data"], t["nav"]))
    langs = " ".join(f'<a href="../{l}/{slug}.html" hreflang="{l}">{name}</a>' for l, name in LANGS.items() if l != lang)
    body = "".join(f"<h2>{h}</h2><p>{c}</p>" if not c.startswith(("<ul", "<ol")) else f"<h2>{h}</h2>{c}" for h, c in sections)
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Entwine</title><link rel="stylesheet" href="../style.css"></head><body><main>
<header><a class="brand" href="../index.html">Entwine</a><nav>{nav}</nav><span class="langs">{langs}</span></header>
<h1>{title}</h1><p class="updated">{t['updated']}: {DATE[lang]}</p>{body}
<footer>Entwine · <a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>
"""

os.makedirs("docs", exist_ok=True)
open("docs/style.css", "w").write(CSS)
open("docs/.nojekyll", "w").write("")
for lang in T:
    os.makedirs(f"docs/{lang}", exist_ok=True)
    t = T[lang]
    for slug, key in [("privacy", "privacy"), ("terms", "terms"), ("delete-data", "delete")]:
        open(f"docs/{lang}/{slug}.html", "w").write(page(lang, slug, t[key + "_title"], t[key]))
    links = "".join(f'<li><a href="{s}.html">{n}</a></li>' for s, n in zip(["privacy", "terms", "delete-data"], t["nav"]))
    open(f"docs/{lang}/index.html", "w").write(page(lang, "index", t["home_title"], [("Entwine", t["home_intro"])]).replace("</p><footer>", "</p>").replace("<footer>", f"<ul>{links}</ul><footer>", 1))

cards = "".join(f'<section><h2>{LANGS[l]}</h2><p>{T[l]["home_intro"]}</p><ul>' + "".join(f'<li><a href="{l}/{s}.html">{n}</a></li>' for s, n in zip(["privacy", "terms", "delete-data"], T[l]["nav"])) + "</ul></section>" for l in T)
open("docs/index.html", "w").write(f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Entwine · Legal</title><link rel="stylesheet" href="style.css"></head><body><main><header><span class="brand">Entwine</span></header>
<h1>Entwine</h1>{cards}<footer><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>
""")
print("ok")
