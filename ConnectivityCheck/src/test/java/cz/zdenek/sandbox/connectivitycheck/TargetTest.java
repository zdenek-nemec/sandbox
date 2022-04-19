package cz.zdenek.sandbox.connectivitycheck;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TargetTest {

    @Test
    void testTargetConstructor() {
        Target target = new Target("login,host,22,description");
        assertEquals("login", target.login);
        assertEquals("host", target.host);
        assertEquals(22, target.port);
        assertEquals("description", target.description);
    }

    @Test
    void testConnectivity() {
    }

    @Test
    void testConnection() {
    }

    @Test
    void getTestReport() {
    }
}
