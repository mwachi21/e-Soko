# images Location

Product images → public/images/products/
Icons / logos → public/images/ui/
Component-specific images → src/assets/

- ProductImage.svelte

## Retrieve the client credentials from the providers

- Create your Google OAuth Client at [Google](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fconsole.cloud.google.com%2Fapis%2Fcredentials%2C&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fapis%2Fcredentials%2C&ifkv=AdBytiPUuIh-G6TD1Q33vbBNhxaRsts_jcZm3f0J9U-YwtEg4QSrpuTM2Mo1l7gTHaeqotYEWzEKxQ&osid=1&passive=1209600&service=cloudconsole&flowName=WebLiteSignIn&flowEntry=ServiceLogin&dsh=S-231695386%3A1753259859847420) make sure to add <http://localhost:5000/google/auth/> into Authorized redirect URIs.
- Create your X Oauth 1.0 Client at [Twitter](https://developer.x.com/en) by creating an app. Add <http://localhost:5000/twitter/auth/> into Authorized redirect URIs.
- Create your Facebook OAuth Client at [Facebook](https://developers.facebook.com/) by creating an app. Add <http://localhost:5000/facebook/auth/> into Authorized redirect URIs.
