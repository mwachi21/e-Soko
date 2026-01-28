# e-Soko

e-Soko is a lightweight online marketplace for buying and selling new, refurbished, and used items.

- Frontend: Svelte
- Backend: Flask
- Database: SQLAlchemy
- Project started: 27 January 2026

## Mission
Enable anyone to quickly list, discover, and purchase items with a simple, trustworthy experience.

## Key User Features

- OAuth sign-in (Google)
- Traditional email/password login
- User dashboard for profile, listings, and orders
- Create, edit, and manage product listings (with photos)
- Account deletion and data export

## Product Model (core fields)

- Title
- Price
- Description
- Condition: New / Refurbished / Used
- Photos
- Category
- Location
- Quantity (optional)
- Status: Draft / Published / Sold

## Next Steps

- Define API endpoints and database models
- Implement authentication (Google OAuth + sessions)
- Build listing creation and dashboard UI in Svelte