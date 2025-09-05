package com.jinternals.ai.demo.services;

import java.util.List;

import lombok.AllArgsConstructor;
import org.springframework.ai.embedding.*;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class EmbeddingService {

    private final EmbeddingModel embeddingModel;

    public float[] createEmbedding(String text) {
        return embeddingModel.embedForResponse(List.of(text))
                .getResults()
                .get(0)
                .getOutput();
    }
}
