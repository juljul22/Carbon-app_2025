from capp import db, application
from capp.models import User, Transport

# Make sure we're inside the Flask application context
with application.app_context():
    # Create all tables (if not already created)
    db.create_all()
# Clear old data (optional for testing)
    User.query.delete()
    Transport.query.delete()
    db.session.commit()

    # Create test users
    user1 = User(username='sabrina', email='sabrina@demo.com', password='sabrina1810')
    user2 = User(username='corrado', email='corrado@demo.com', password='corri1709')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create test transport data for user1
    transport1 = Transport(kms=1, transport='car', fuel='diesel', co2=1, ch4=0.5, total=1.5, user_id=user1.id)
    transport2 = Transport(kms=1, transport='boat', fuel='none', co2=1, ch4=1, total=0, user_id=user1.id)
    transport3 = Transport(kms=1, transport='plane', fuel='diesel', co2=3, ch4=1, total=4, user_id=user1.id)
    transport4 = Transport(kms=1, transport='bus', fuel='petrol', co2=1, ch4=1, total=2, user_id=user1.id)
    transport5 = Transport(kms=1, transport='train', fuel='xx', co2=1, ch4=1, total=2, user_id=user1.id)
    transport6 = Transport(kms=1, transport='foot', fuel='xx', co2=1, ch4=1, total=2, user_id=user1.id)

    db.session.add_all([transport1, transport2, transport3, transport4, transport5, transport6])
    db.session.commit()

    print("✅ Database created and test data inserted successfully!")
