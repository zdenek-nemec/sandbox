package com.example.akkademo;

import io.opentelemetry.sdk.common.CompletableResultCode;
import io.opentelemetry.sdk.trace.data.SpanData;
import io.opentelemetry.sdk.trace.export.SpanExporter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Collection;

/** Exports completed spans to SLF4J so they appear alongside Akka's actor logs. */
class Slf4jSpanExporter implements SpanExporter {

    private static final Logger log = LoggerFactory.getLogger(Slf4jSpanExporter.class);
    private static final String NO_PARENT = "0000000000000000";

    @Override
    public CompletableResultCode export(Collection<SpanData> spans) {
        for (SpanData s : spans) {
            String parent = NO_PARENT.equals(s.getParentSpanId()) ? "none" : s.getParentSpanId();
            long durationMs = (s.getEndEpochNanos() - s.getStartEpochNanos()) / 1_000_000;
            log.info("[SPAN] \"{}\"  trace={}  span={}  parent={}  {}ms",
                    s.getName(), s.getTraceId(), s.getSpanId(), parent, durationMs);
        }
        return CompletableResultCode.ofSuccess();
    }

    @Override
    public CompletableResultCode flush() {
        return CompletableResultCode.ofSuccess();
    }

    @Override
    public CompletableResultCode shutdown() {
        return CompletableResultCode.ofSuccess();
    }
}
