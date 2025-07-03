const request = require('supertest');
const app = require('../backend/server');

describe('Middleware authenticateToken', () => {
  it('devrait refuser l\'accès avec un token invalide', async () => {
    const res = await request(app)
      .get('/api/tasks')
      .set('Authorization', 'Bearer FAUXTOKEN123');

    expect(res.statusCode).toBe(403);
    expect(res.body).toHaveProperty('error', 'Token invalide');
  });

  it('devrait refuser l\'accès sans token', async () => {
    const res = await request(app)
      .get('/api/tasks');

    expect(res.statusCode).toBe(401);
    expect(res.body).toHaveProperty('error', 'Token d\'accès requis');
  });
});
